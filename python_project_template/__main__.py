"""python-project-template: Launcher.

© Reuben Thomas <rrt@sc3d.org> 2025.

Released under the GPL version 3, or (at your option) any later version.
"""

import re
import sys

from python_project_template import main


sys.argv[0] = re.sub(r"__main__.py$", "python_project_template", sys.argv[0])
main()
