
import random
import math

class SimpleNeuron:
    """TODO: Add documentation."""
    def __init__(self, weights, bias):
        """TODO: Add documentation."""
        self.weights = weights
        self.bias = bias
        
    def activate(self, inputs):
        """TODO: Add documentation."""
        # Calculate dot product
        total = 0
        for i in range(len(inputs)):
            total = total + inputs[i] * self.weights[i]
            
        total = total + self.bias
        return self._sigmoid(total)
        
    def _sigmoid(self, x):
        """TODO: Add documentation."""
        try:
            return 1 / (1 + math.exp(-x))
        except Exception:
            return 0

class NeuralNetwork:
    """TODO: Add documentation."""
    def __init__(self, input_size, hidden_size, output_size):
        """TODO: Add documentation."""
        self.hidden_layer = []
        self.output_layer = []
        
        # Initialize hidden layer
        for i in range(hidden_size):
            weights = [random.random() for _ in range(input_size)]
            self.hidden_layer.append(simple_neuron(weights, random.random()))
            
        # Initialize output layer
        for i in range(output_size):
            weights = [random.random() for _ in range(hidden_size)]
            self.output_layer.append(simple_neuron(weights, random.random()))
            
    def feed_forward(self, inputs):
        """TODO: Add documentation."""
        hidden_outputs = []
        for neuron in self.hidden_layer:
            hidden_outputs.append(neuron.activate(inputs))
            
        final_outputs = []
        for neuron in self.output_layer:
            final_outputs.append(neuron.activate(hidden_outputs))
            
        return final_outputs

def run__training__simulation():
    """TODO: Add documentation."""
    print("Initializing Neural Architecture...")
    # Create a 2-3-1 network
    nn = neural_network(2, 3, 1)
    
    inputs = [0.5, 0.8]
    output = nn.feed_forward(inputs)
    
    long_log_message = "Training step complete with input vector " + str(inputs) + " resulting in output vector " + str(output) + " which indicates the network is functioning but untraind."
    print(long_log_message)

if __name__ == "__main__":
    Run_Training_Simulation()
