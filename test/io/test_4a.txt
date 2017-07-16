#!../apl.py -f
'Test ⎕← (output operator)'

1
1 + 2
⎕ ← 2
⎕ ← 1 + 2
1 + ⎕ ← 2
1 + ⎕ ← 2 + 3
⎕ ← ⎕ ← 1
1 + ⎕ ← ⎕ ← 2

)OFF
