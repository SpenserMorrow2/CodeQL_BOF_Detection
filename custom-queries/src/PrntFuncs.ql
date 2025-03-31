/**
 * @name All function calls
 * @description Lists all function calls found in the codebase.
 * @id custom.prnts
 * @kind problem
 * @problem.severity recommendation
 */

import cpp

from FunctionCall call
select call, "Function call to " + call.getTarget().getName()
