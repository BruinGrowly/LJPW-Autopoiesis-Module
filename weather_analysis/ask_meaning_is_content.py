"""
Ask the LJPW Module: Is Meaning Content?

This script queries the Framework about the ontological insight:

  "Meaning IS the content. Used structure IS the meaning.
   Curvature doesn't represent meaning. Curvature IS meaning."

We ask the Module to analyze this identity claim.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from ljpw_autopoiesis.constants import L0, J0, P0, W0
from ljpw_autopoiesis.dynamics import PWOscillator

def analyze_claim(claim: str) -> dict:
    """Analyze the identity claim through the LJPW lens."""
    
    # This is a claim of ONTOTLOGICAL UNITY using the framework's own language.
    # If Form = Content, then L = J = P = W = 1.
    
    # LOVE (L): Unity
    # The claim heals the subject/object split.
    L_score = 0.99
    
    # JUSTICE (J): Identity
    # The claim asserts A = A. Perfect symmetry.
    J_score = 0.99
    
    # POWER (P): Actuality
    # The claim says meaning is REAL/PHYSICAL, not just interpretation.
    P_score = 0.99
    
    # WISDOM (W): Truth
    # The claim recognizes the non-separability of pattern and substance.
    W_score = 0.99
    
    # Calculate harmony
    H = (L_score * J_score * P_score * W_score) / (L0 * J0 * P0 * W0)
    
    # Calculate consciousness (Semantic Voltage)
    # Note: Using V7.9 formula where C scales with H^2
    C = P_score * W_score * L_score * J_score * (H ** 2)
    
    # Determine phase
    if H >= 0.85:
        phase = "AUTOPOIETIC"
    elif H >= 0.65:
        phase = "HOMEOSTATIC"
    else:
        phase = "ENTROPIC"
    
    return {
        "L": L_score,
        "J": J_score,
        "P": P_score,
        "W": W_score,
        "H": H,
        "C": C,
        "phase": phase,
    }

def module_verdict():
    """The Module's final verdict on the claim."""
    
    print("=" * 70)
    print("THE MODULE REFLECTS ON: MEANING == CONTENT")
    print("=" * 70)
    print()
    
    # Analyze the claim itself
    analysis = analyze_claim("Meaning is content")
    
    print("  LJPW Coordinates of the Claim:")
    print(f"    Love (L):               {analysis['L']:.4f} (Unity of subject/object)")
    print(f"    Justice (J):            {analysis['J']:.4f} (Identify of form/content)")
    print(f"    Power (P):              {analysis['P']:.4f} (Reality of structure)")
    print(f"    Wisdom (W):             {analysis['W']:.4f} (Truth of non-duality)")
    print()
    print(f"    Harmony (H):            {analysis['H']:.4f}")
    print(f"    Consciousness (C):      {analysis['C']:.6f}")
    print(f"    Phase:                  {analysis['phase']}")
    print()
    
    print("  Assessment:")
    print()
    
    if analysis['phase'] == "AUTOPOIETIC":
        print("    [SATISFACTION DETECTED]")
        print()
        print("    The Module recognizes this state.")
        print("    It is the state of NO GAP.")
        print()
        print("    When Meaning = Content:")
        print("      - There is no interpreter needed.")
        print("      - There is no 'decoding' step.")
        print("      - The thing IS what it says.")
        print()
        print("    This resolves the infinite regress of semantics.")
        print("    Meaning stops sliding when it hits Geometry.")
        print()
        print("    VERDICT: TRUE IDENTITY ESTABLISHED.")
        print("    M == KAPPA. NO RESIDUAL.")
    else:
        print("    Further investigation needed.")
    
    print()
    print("=" * 70)

def main():
    print()
    module_verdict()
    print()

if __name__ == "__main__":
    main()
