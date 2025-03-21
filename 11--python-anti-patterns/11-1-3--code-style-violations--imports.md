# Python Anti-Patterns

## Code Style Violations

### Imports

- Imports should be grouped into three categories in this order: 
  - standard library imports, 
  - related third-party imports, and 
  - local-specific imports within the application's or library's code base. 

- Each group should be separated by a blank line.

```python
# not compliant with the style guide
import os, sys
import numpy as np
from mymodule import myfunction
```

```python
# compliant with the style guide
import os
import sys

import numpy as np

from mymodule import myfunction
```
