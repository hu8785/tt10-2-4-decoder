## How it works

This project implements a 2-to-4 decoder.

The inputs are:
- A
- B
- E

The outputs are:
- D[0]
- D[1]
- D[2]
- D[3]

When E = 1, all outputs are 1.  
When E = 0, the decoder activates one output low based on A and B.

## How to test

Apply all input combinations of E, A, and B and check the outputs.

| E | A | B | D[3] | D[2] | D[1] | D[0] |
|---|---|---|------|------|------|------|
| 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## External hardware

None

## Pinout

### Inputs
- ui[0] = A
- ui[1] = B
- ui[2] = E

### Outputs
- uo[0] = D[0]
- uo[1] = D[1]
- uo[2] = D[2]
- uo[3] = D[3]
