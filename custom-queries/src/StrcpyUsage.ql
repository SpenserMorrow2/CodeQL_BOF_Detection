/**
 * @name Use of strcpy (unsafe)
 * @description Detects calls to strcpy, which can cause buffer overflows.
 * @id custom.strcpy-usage
 * @kind problem
 * @problem.severity warning
 */

import cpp

from FunctionCall call
where call.getTarget().getName() = "strcpy"
select call, "Unsafe use of 'strcpy' detected. This may lead to a buffer overflow."
