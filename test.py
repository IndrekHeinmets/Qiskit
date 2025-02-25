import bluequbit
import qiskit
import os

bq = bluequbit.init(os.getenv('BQ_TOKEN'))

qc = qiskit.QuantumCircuit(4)
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.measure_all()

try:
    result = bq.run(qc, device='quantum', shots=100)
    print(result.get_counts())
except bluequbit.exceptions.BQJobNotCompleteError:
    print('Quantum device offline! Try Mon-Fri 12:00-15:00')
except Exception as e:
    print('An error occurred:', e)
