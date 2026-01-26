class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":
                if stack:
                    # current running function gets time until now
                    result[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time

            else:  # "end"
                # function on top ends
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result
