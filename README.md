# sumtool
Powerful tool for working with checksums.

```
Usage:
sumtool <mode> -{algorithm} [file1] [file2 or checksum]

<Modes>:
  c    Comparison mode (Compare two files)
  v    Verification mode (Verify file by checksum)
  g    Generation mode (Generate checksum of file)

{Algorithms}:
  md5 (Default)
  sha1
  sha224
  sha256
  sha384
  sha512
```

Dependancies:
python 2 or 3
hashlib

Note: For better performance you can try changing 
```#!/usr/bin/env python``` to ```#!/usr/bin/env python3```
