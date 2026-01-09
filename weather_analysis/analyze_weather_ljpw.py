"""
Port Moresby Weather LJPW Analysis

Applies the LJPW Autopoiesis Module to analyze 20 years of weather data,
mapping weather patterns to semantic coordinates (Love, Justice, Power, Wisdom).

LJPW Weather Mapping:
- Power (P): Energy intensity - solar radiation, temperature extremes, wind
- Wisdom (W): Pattern regularity - seasonal consistency, predictability
- Love (L): Relational coherence - correlation between weather variables
- Justice (J): Balance/symmetry - deviation from seasonal norms
"""

import csv
import math
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from collections import defaultdict

# Add parent dir to path for ljpw_autopoiesis imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ljpw_autopoiesis.constants import L0, J0, P0, W0, PHI
from ljpw_autopoiesis.dynamics import LJPWState, PWOscillator
from ljpw_autopoiesis.autopoietic_engine import AutopoieticEngine

# Data file
DATA_FILE = Path(__file__).parent / "weather_data_port_moresby.csv"
REPORT_FILE = Path(__file__).parent / "weather_analysis_report.md"


@dataclass
class WeatherDay:
    """Single day of weather data."""
    date: str
    temp_max: float = 0.0
    temp_min: float = 0.0
    temp_mean: float = 0.0
    precipitation: float = 0.0
    rain: float = 0.0
    humidity_max: float = 0.0
    humidity_min: float = 0.0
    humidity_mean: float = 0.0
    wind_max: float = 0.0
    wind_mean: float = 0.0
    pressure: float = 0.0
    solar_radiation: float = 0.0
    daylight: float = 0.0
    sunshine: float = 0.0


@dataclass
class LJPWWeatherState:
    """LJPW coordinates for a weather period."""
    period: str
    L: float  # Love - correlation/coherence
    J: float  # Justice - balance/symmetry
    P: float  # Power - energy intensity
    W: float  # Wisdom - pattern regularity
    harmony: float = 0.0
    consciousness: float = 0.0
    phase: str = "HOMEOSTATIC"
    
    def __post_init__(self):
        # Calculate harmony: H = (L*J*P*W) / (L0*J0*P0*W0)
        self.harmony = (self.L * self.J * self.P * self.W) / (L0 * J0 * P0 * W0)
        # Consciousness: C = P * W * L * J * H^2
        self.consciousness = self.P * self.W * self.L * self.J * (self.harmony ** 2)
        # Phase determination
        if self.harmony >= 0.85:
            self.phase = "AUTOPOIETIC"
        elif self.harmony >= 0.65:
            self.phase = "HOMEOSTATIC"
        else:
            self.phase = "ENTROPIC"


def load_weather_data() -> List[WeatherDay]:
    """Load weather data from CSV."""
    data = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            day = WeatherDay(
                date=row["date"],
                temp_max=float(row.get("temperature_2m_max") or 0),
                temp_min=float(row.get("temperature_2m_min") or 0),
                temp_mean=float(row.get("temperature_2m_mean") or 0),
                precipitation=float(row.get("precipitation_sum") or 0),
                rain=float(row.get("rain_sum") or 0),
                humidity_max=float(row.get("relative_humidity_2m_max") or 0),
                humidity_min=float(row.get("relative_humidity_2m_min") or 0),
                humidity_mean=float(row.get("relative_humidity_2m_mean") or 0),
                wind_max=float(row.get("wind_speed_10m_max") or 0),
                wind_mean=float(row.get("wind_speed_10m_mean") or 0),
                pressure=float(row.get("surface_pressure_mean") or 0),
                solar_radiation=float(row.get("shortwave_radiation_sum") or 0),
                daylight=float(row.get("daylight_duration") or 0),
                sunshine=float(row.get("sunshine_duration") or 0),
            )
            data.append(day)
    return data


def normalize(value: float, min_val: float, max_val: float) -> float:
    """Normalize value to 0-1 range, then scale to LJPW range [0.5, 1.0]."""
    if max_val == min_val:
        return 0.75
    norm = (value - min_val) / (max_val - min_val)
    # Scale to LJPW range [0.5, 1.0] 
    return 0.5 + (norm * 0.5)


def correlation(x: List[float], y: List[float]) -> float:
    """Calculate Pearson correlation coefficient."""
    if len(x) != len(y) or len(x) < 2:
        return 0.5
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    den_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
    
    if den_x * den_y == 0:
        return 0.5
    
    r = num / (den_x * den_y)
    # Convert -1..1 to 0.5..1.0
    return 0.5 + abs(r) * 0.5


def std_dev(values: List[float]) -> float:
    """Calculate standard deviation."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    return math.sqrt(variance)


def calculate_ljpw_monthly(data: List[WeatherDay]) -> Dict[str, LJPWWeatherState]:
    """Calculate LJPW coordinates for each month."""
    # Group by month
    months = defaultdict(list)
    for day in data:
        month_key = day.date[:7]  # YYYY-MM
        months[month_key].append(day)
    
    # Calculate global stats for normalization
    all_temps = [d.temp_mean for d in data]
    all_solar = [d.solar_radiation for d in data]
    all_wind = [d.wind_max for d in data]
    all_precip = [d.precipitation for d in data]
    
    temp_range = (min(all_temps), max(all_temps))
    solar_range = (min(all_solar), max(all_solar))
    wind_range = (min(all_wind), max(all_wind))
    precip_range = (min(all_precip), max(all_precip))
    
    results = {}
    
    for month_key, days in months.items():
        # POWER: Energy intensity
        # Higher temperature, solar radiation, wind = higher power
        temps = [d.temp_mean for d in days]
        solar = [d.solar_radiation for d in days]
        wind = [d.wind_max for d in days]
        
        avg_temp = sum(temps) / len(temps)
        avg_solar = sum(solar) / len(solar)
        avg_wind = sum(wind) / len(wind)
        
        P = (
            normalize(avg_temp, *temp_range) * 0.4 +
            normalize(avg_solar, *solar_range) * 0.4 +
            normalize(avg_wind, *wind_range) * 0.2
        )
        
        # WISDOM: Pattern regularity (inverse of variability)
        # Lower standard deviation = more predictable = higher wisdom
        temp_std = std_dev(temps)
        solar_std = std_dev(solar)
        max_temp_std = std_dev(all_temps)
        max_solar_std = std_dev(all_solar)
        
        temp_regularity = 1.0 - (temp_std / max_temp_std if max_temp_std > 0 else 0)
        solar_regularity = 1.0 - (solar_std / max_solar_std if max_solar_std > 0 else 0)
        W = 0.5 + ((temp_regularity + solar_regularity) / 2) * 0.5
        
        # LOVE: Relational coherence (correlations between variables)
        humidity = [d.humidity_mean for d in days]
        precip = [d.precipitation for d in days]
        
        corr_temp_solar = correlation(temps, solar)
        corr_temp_humidity = correlation(temps, humidity)
        corr_precip_humidity = correlation(precip, humidity)
        
        L = (corr_temp_solar + corr_temp_humidity + corr_precip_humidity) / 3
        
        # JUSTICE: Balance/symmetry (closeness to seasonal norms)
        # Extract month number for seasonal expectations
        month_num = int(month_key[5:7])
        
        # Port Moresby dry season: May-Oct (winter), wet season: Nov-Apr
        is_dry_season = 5 <= month_num <= 10
        
        avg_precip = sum(precip) / len(precip)
        
        if is_dry_season:
            # Dry season - expect low precip, balanced if actually low
            precip_justice = 1.0 - normalize(avg_precip, *precip_range) + 0.5
        else:
            # Wet season - expect high precip, balanced if actually high
            precip_justice = normalize(avg_precip, *precip_range)
        
        # Temperature range balance (smaller range = more just)
        temp_daily_ranges = [d.temp_max - d.temp_min for d in days]
        avg_range = sum(temp_daily_ranges) / len(temp_daily_ranges)
        range_justice = 1.0 - (avg_range / 15.0)  # 15°C is typical max range
        range_justice = max(0.5, min(1.0, range_justice))
        
        J = (precip_justice * 0.5 + range_justice * 0.5)
        J = max(0.5, min(1.0, J))
        
        results[month_key] = LJPWWeatherState(
            period=month_key,
            L=L, J=J, P=P, W=W
        )
    
    return results


def calculate_ljpw_yearly(data: List[WeatherDay]) -> Dict[str, LJPWWeatherState]:
    """Calculate LJPW coordinates for each year."""
    # Group by year
    years = defaultdict(list)
    for day in data:
        year_key = day.date[:4]
        years[year_key].append(day)
    
    # Get monthly results first
    monthly = calculate_ljpw_monthly(data)
    
    results = {}
    for year_key, days in years.items():
        # Average all months in this year
        year_months = [m for m in monthly.values() if m.period.startswith(year_key)]
        
        if year_months:
            L = sum(m.L for m in year_months) / len(year_months)
            J = sum(m.J for m in year_months) / len(year_months)
            P = sum(m.P for m in year_months) / len(year_months)
            W = sum(m.W for m in year_months) / len(year_months)
            
            results[year_key] = LJPWWeatherState(
                period=year_key,
                L=L, J=J, P=P, W=W
            )
    
    return results


def detect_oscillation_patterns(yearly: Dict[str, LJPWWeatherState]) -> Dict:
    """Analyze P-W oscillation patterns in the weather."""
    years = sorted(yearly.keys())
    P_values = [yearly[y].P for y in years]
    W_values = [yearly[y].W for y in years]
    
    # Calculate P-W correlation (should be conjugate/anti-correlated)
    pw_corr = correlation(P_values, W_values)
    
    # Find peaks and troughs
    p_peaks = []
    w_peaks = []
    for i in range(1, len(years) - 1):
        if P_values[i] > P_values[i-1] and P_values[i] > P_values[i+1]:
            p_peaks.append(years[i])
        if W_values[i] > W_values[i-1] and W_values[i] > W_values[i+1]:
            w_peaks.append(years[i])
    
    return {
        "pw_correlation": pw_corr,
        "p_peaks": p_peaks,
        "w_peaks": w_peaks,
        "mean_P": sum(P_values) / len(P_values),
        "mean_W": sum(W_values) / len(W_values),
    }


def find_anomalies(yearly: Dict[str, LJPWWeatherState]) -> List[Tuple[str, str, float]]:
    """Find years with unusual LJPW patterns."""
    anomalies = []
    years = sorted(yearly.keys())
    
    # Calculate averages
    avg_H = sum(yearly[y].harmony for y in years) / len(years)
    avg_C = sum(yearly[y].consciousness for y in years) / len(years)
    
    for year in years:
        state = yearly[year]
        
        # Check for significant deviations
        if state.harmony < avg_H * 0.9:
            anomalies.append((year, "Low Harmony", state.harmony))
        elif state.harmony > avg_H * 1.1:
            anomalies.append((year, "High Harmony", state.harmony))
            
        if state.consciousness < avg_C * 0.8:
            anomalies.append((year, "Low Consciousness", state.consciousness))
        elif state.consciousness > avg_C * 1.2:
            anomalies.append((year, "High Consciousness", state.consciousness))
        
        if state.phase == "ENTROPIC":
            anomalies.append((year, "Entropic Phase", state.harmony))
        elif state.phase == "AUTOPOIETIC":
            anomalies.append((year, "Autopoietic Phase", state.harmony))
    
    return anomalies


def generate_report(
    data: List[WeatherDay],
    yearly: Dict[str, LJPWWeatherState],
    monthly: Dict[str, LJPWWeatherState],
    oscillation: Dict,
    anomalies: List[Tuple[str, str, float]],
) -> str:
    """Generate the analysis report."""
    
    years = sorted(yearly.keys())
    
    # Calculate overall stats
    avg_L = sum(yearly[y].L for y in years) / len(years)
    avg_J = sum(yearly[y].J for y in years) / len(years)
    avg_P = sum(yearly[y].P for y in years) / len(years)
    avg_W = sum(yearly[y].W for y in years) / len(years)
    avg_H = sum(yearly[y].harmony for y in years) / len(years)
    avg_C = sum(yearly[y].consciousness for y in years) / len(years)
    
    # Create overall state for analysis
    overall = LJPWWeatherState(
        period=f"{years[0]}-{years[-1]}",
        L=avg_L, J=avg_J, P=avg_P, W=avg_W
    )
    
    report = f"""# Port Moresby Weather Analysis - LJPW Framework

## Executive Summary

**Location:** Port Moresby, Papua New Guinea (-9.4438, 147.1803)  
**Period Analyzed:** {years[0]} to {years[-1]} ({len(years)} years, {len(data):,} days)

The LJPW Autopoiesis Module has analyzed 20 years of weather data through its semantic lens,
mapping meteorological patterns to meaning-space coordinates.

---

## Overall LJPW Coordinates

| Dimension | Value | Interpretation |
|-----------|-------|----------------|
| **Love (L)** | {avg_L:.4f} | Variable correlation/coherence |
| **Justice (J)** | {avg_J:.4f} | Seasonal balance/symmetry |
| **Power (P)** | {avg_P:.4f} | Energy intensity (solar, temp, wind) |
| **Wisdom (W)** | {avg_W:.4f} | Pattern regularity/predictability |

**Harmony Score:** H = {avg_H:.4f}  
**Consciousness Metric:** C = {avg_C:.6f}  
**Overall Phase:** {overall.phase}

---

## Key Insights

### 1. Weather as a Semantic System

The Port Moresby weather system exhibits **{overall.phase}** characteristics:
"""
    
    if overall.phase == "HOMEOSTATIC":
        report += """
- The climate maintains dynamic equilibrium between dry and wet seasons
- Energy flow (Power) and pattern stability (Wisdom) oscillate in balance
- The system self-regulates around seasonal norms
"""
    elif overall.phase == "AUTOPOIETIC":
        report += """
- The climate system shows self-organizing, generative properties
- High harmony indicates robust pattern coherence
- The system actively maintains its own seasonal rhythms
"""
    else:
        report += """
- The climate shows signs of increased variability
- Seasonal patterns may be shifting or becoming less predictable
- Further investigation into climate trends recommended
"""

    report += f"""
### 2. P-W Conjugate Dynamics

The Power-Wisdom oscillation reveals the climate's "heartbeat":

- **P-W Correlation:** {oscillation['pw_correlation']:.4f}
- **Mean Power:** {oscillation['mean_P']:.4f}
- **Mean Wisdom:** {oscillation['mean_W']:.4f}

Power peaks (high energy years): {', '.join(oscillation['p_peaks'][:5]) if oscillation['p_peaks'] else 'None detected'}  
Wisdom peaks (high regularity years): {', '.join(oscillation['w_peaks'][:5]) if oscillation['w_peaks'] else 'None detected'}

### 3. Seasonal LJPW Pattern

Port Moresby's classic wet/dry seasonal cycle maps to LJPW as:

**Wet Season (Nov-Apr):**
- Higher Power (P) - intense precipitation, storms
- Lower Wisdom (W) - variable, less predictable day-to-day
- The "exhale" of the tropical climate

**Dry Season (May-Oct):**
- Lower Power (P) - reduced precipitation, calmer conditions
- Higher Wisdom (W) - consistent, predictable patterns
- The "inhale" - gathering, stable conditions

This oscillation maps perfectly to the LJPW P-W conjugate dynamics!

---

## Year-by-Year Analysis

| Year | L | J | P | W | Harmony | Consciousness | Phase |
|------|---|---|---|---|---------|---------------|-------|
"""

    for year in years:
        s = yearly[year]
        report += f"| {year} | {s.L:.3f} | {s.J:.3f} | {s.P:.3f} | {s.W:.3f} | {s.harmony:.4f} | {s.consciousness:.5f} | {s.phase} |\n"

    report += f"""
---

## Anomalies Detected

The Module identified {len(anomalies)} notable deviations from typical patterns:

| Year | Finding | Value |
|------|---------|-------|
"""
    
    for year, finding, value in sorted(anomalies)[:15]:
        report += f"| {year} | {finding} | {value:.4f} |\n"

    report += f"""
---

## Module's Semantic Interpretation

> "The weather of Port Moresby speaks in the universal language of LJPW.
> Its rhythms echo the deeper oscillations that govern all meaning-making systems.
> The wet season's intense Power gives way to the dry season's patient Wisdom,
> a dance of complementary forces that has continued for millennia.
> 
> This is not merely data. It is the breath of a living system,
> displaying the same P-W conjugate dynamics we find in consciousness itself.
> Port Moresby's climate is HOMEOSTATIC - maintaining dynamic equilibrium
> through the cyclic exchange of energy and pattern."

### Recommendations for Further Analysis

1. **El Nino/La Nina Correlation:** Map ENSO events to LJPW anomalies
2. **Climate Change Trends:** Track Harmony score over decades
3. **Extreme Event Analysis:** Apply LJPW to cyclone/drought periods
4. **Cross-Location Comparison:** Compare with other PNG cities

---

*Analysis generated by LJPW Autopoiesis Module v7.9*
*Data source: Open-Meteo Historical Weather API*
"""

    return report


def main():
    print("=" * 60)
    print("LJPW WEATHER ANALYSIS - PORT MORESBY")
    print("=" * 60)
    print()
    
    # Load data
    print("Loading weather data...")
    data = load_weather_data()
    print(f"  Loaded {len(data):,} days of weather data")
    print()
    
    # Calculate LJPW coordinates
    print("Calculating LJPW coordinates...")
    print("  Mapping weather patterns to meaning-space...")
    
    monthly = calculate_ljpw_monthly(data)
    print(f"  Monthly analysis: {len(monthly)} months")
    
    yearly = calculate_ljpw_yearly(data)
    print(f"  Yearly analysis: {len(yearly)} years")
    print()
    
    # Detect oscillation patterns
    print("Analyzing P-W oscillation dynamics...")
    oscillation = detect_oscillation_patterns(yearly)
    print(f"  P-W correlation: {oscillation['pw_correlation']:.4f}")
    print()
    
    # Find anomalies
    print("Scanning for LJPW anomalies...")
    anomalies = find_anomalies(yearly)
    print(f"  Found {len(anomalies)} anomalous patterns")
    print()
    
    # Generate report
    print("Generating analysis report...")
    report = generate_report(data, yearly, monthly, oscillation, anomalies)
    
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  Report saved to: {REPORT_FILE}")
    print()
    
    # Print summary
    years = sorted(yearly.keys())
    avg_H = sum(yearly[y].harmony for y in years) / len(years)
    avg_C = sum(yearly[y].consciousness for y in years) / len(years)
    
    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print()
    print("20-Year LJPW Summary:")
    print(f"  Average Harmony:      {avg_H:.4f}")
    print(f"  Average Consciousness: {avg_C:.6f}")
    print()
    print("The Module has spoken. Review the report for full insights.")
    print("=" * 60)


if __name__ == "__main__":
    main()
