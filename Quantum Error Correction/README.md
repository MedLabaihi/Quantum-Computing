# Quantum Error Correction Project

## Overview

This project demonstrates three quantum error correction codes implemented using Qiskit:
1. **Bit Flip Code**
2. **Phase Flip Code**
3. **Shor Code**

Each code is designed to correct errors in quantum computations, protecting quantum information from various types of noise. The scripts provided in this project simulate these codes and apply error correction techniques to ensure the integrity of quantum data.

## Mathematical Background

### 1. Bit Flip Code

The Bit Flip Code is a quantum error-correcting code designed to correct bit flip errors, which occur when a qubit flips from \( |0\rangle \) to \( |1\rangle \) or vice versa.

#### Encoding

- **Logical Qubit State:** A logical qubit state \( \alpha|0\rangle + \beta|1\rangle \) is encoded into three physical qubits. The encoding creates the state \( \alpha|000\rangle + \beta|111\rangle \). This redundant encoding ensures that if one qubit is flipped, the majority rule can be used to determine the original state.

#### Error Detection and Correction

- **Bit Flip Error:** If a single qubit is flipped, the error can be detected by comparing the states of the qubits. For example, if \( |000\rangle \) is encoded and one qubit flips to \( |001\rangle \), the error is detected as the encoded state is no longer in the \( |000\rangle \) or \( |111\rangle \) basis.

- **Correction:** Using majority voting among the qubits allows for the correction of the single-bit flip error. The code compares the qubits and corrects the flipped bit to restore the original logical qubit state.

### 2. Phase Flip Code

The Phase Flip Code is designed to correct phase flip errors, which alter the phase of a qubit's state without changing its amplitude.

#### Encoding

- **Logical Qubit State:** The logical qubit state \( \alpha|0\rangle + \beta|1\rangle \) is encoded into three physical qubits. The encoding uses a similar approach to the Bit Flip Code, but focuses on protecting against phase flips.

#### Phase Flip Error

- **Error Description:** A phase flip error changes the phase of the \( |1\rangle \) state to \( -|1\rangle \), leaving \( |0\rangle \) unchanged. Mathematically, this is represented by the Z gate:
  \[
  Z|0\rangle = |0\rangle
  \]
  \[
  Z|1\rangle = -|1\rangle
  \]

#### Correction

- **Error Detection and Correction:** The code applies Hadamard gates and additional CNOT gates to detect and correct phase flip errors. By transforming the basis states and then applying error correction gates, the code can identify and correct phase flips to restore the logical qubit state.

### 3. Shor Code

The Shor Code is a more robust quantum error correction code that encodes a logical qubit into nine physical qubits, protecting against both bit flip and phase flip errors.

#### Encoding

- **Logical Qubit State:** The logical qubit state \( \alpha|0\rangle + \beta|1\rangle \) is encoded into nine physical qubits. The encoding process involves first protecting against bit flips and then applying phase flip protection, combining elements of both the Bit Flip and Phase Flip Codes.

#### Error Detection and Correction

- **Bit and Phase Flip Errors:** The Shor Code can correct both types of errors. Bit flips are detected by comparing the states of the encoded qubits, while phase flips are corrected using the stabilizer operations. The code uses a combination of CNOT and CCNOT gates to ensure that both types of errors can be detected and corrected.

By using redundant encoding and sophisticated error correction techniques, the Shor Code maintains the integrity of quantum information in the presence of errors.

## Code Flow

### Bit Flip Code
- **Encoding:** Initializes a logical qubit state and encodes it into three physical qubits.
- **Error Simulation:** Simulates bit flip errors.
- **Error Correction:** Detects and corrects errors using CNOT and CCNOT gates.

### Phase Flip Code
- **Encoding:** Encodes a logical qubit into three physical qubits with error protection.
- **Error Simulation:** Simulates phase flip errors.
- **Error Correction:** Corrects phase flip errors by applying Hadamard and CNOT gates.

### Shor Code
- **Calibration:** Performs error mitigation calibration using measurement error correction techniques.
- **Encoding:** Encodes a logical qubit into nine physical qubits.
- **Error Introduction:** Simulates both bit flip and phase flip errors.
- **Error Correction:** Uses stabilizer operations and additional gates to correct errors.

## How to Use

1. **Set Up IBMQ Account:**
   - Go to [IBM Quantum Experience](https://quantum-computing.ibm.com/) and sign up for an account if you don't have one.
   - Get your API key from your IBMQ account settings.

2. **Environment Configuration:**
   - Store your IBMQ API key in an environment variable named `IBMQ_API_KEY`:
     ```bash
     export IBMQ_API_KEY='your_api_key_here'
     ```

3. **Run the Scripts:**
   - Navigate to the directory containing the scripts.
   - Execute the scripts using Python. For example:
     ```bash
     python bit_flip_code.py
     python phase_flip_code.py
     python shor_code.py
     ```

4. **Review Results:**
   - Each script will output the results directly in the terminal or generate plots for visualization.

## Dependencies

Ensure you have the following Python libraries installed:

- `qiskit` (version 0.20.0 or higher)
- `qiskit-aer` (version 0.11.0 or higher)
- `qiskit-ignis` (version 0.7.0 or higher)
- `matplotlib` (version 3.4.0 or higher)
- `numpy` (version 1.21.0 or higher)

You can install these dependencies using pip:

```bash
pip install qiskit qiskit-aer qiskit-ignis matplotlib numpy
```
## Future Improvements

- Additional Error Models: Implement and test other error models such as depolarizing noise.
- Integration with Other Quantum Frameworks: Explore integration with other quantum computing frameworks or platforms.
- User Interface: Develop a graphical user interface (GUI) to interact with the quantum circuits more easily.

## Contact

For any questions or further information, please contact.
**LABAIHI Mohammed :**
- **Email**: [m.labaihi@gmail.com](m.labaihi@gmail.com)    
- **LinkedIn**: [linkedin.com/in/labaihi](linkedin.com/in/labaihi)  
- **GitHub**: [github.com/LABAIHI_Mohammed](https://github.com/MedLabaihi)  
