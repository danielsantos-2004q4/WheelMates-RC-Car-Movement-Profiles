-- Build: 1713cbeb8a7efe2f61674448516d1383
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
