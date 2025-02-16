"""$include{project_name.in.py}: Main module.

© $include{author.in.py} <$include{email.in.py}> $include{year.in.py}
Released under the GPL version 3, or (at your option) any later version.
"""

import re
import sys

from $include{project_slug.in.py} import main


sys.argv[0] = re.sub(r"__main__.py$", "$include{project_slug.in.py}", sys.argv[0])
main()
