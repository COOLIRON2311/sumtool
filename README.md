# sumtool
Powerful tool for working with checksums.

```
Usage:
sumtool <mode> -{algorithm} [file1 or checksum] [file2 or checksum]

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
  crc32
```

#### Dependencies:
```
python (>=2)
```

#### Note:
For better performance you can try changing 
```#!/usr/bin/env python``` to ```#!/usr/bin/env python3```

#### Additional settings:
By default, crc32 case is ```crc_case = 'upper'```. You can change it to ```crc_case = 'lower'``` if you want the output to be  ```ce76b455``` instead of ```CE76B455```.
