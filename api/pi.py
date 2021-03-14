from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib.parse import urlparse, parse_qs

def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


def main(q):  # Wrapper function

    # Calls CalcPi with the given limit
    pi_digits = calcPi(int(q))

    # Prints the output of calcPi generator function
    digs = []
    for d in pi_digits:
        digs.append(d)
    txt = ""
    for g in digs:
      txt += str(g)
    return txt

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    query_components = parse_qs(urlparse(self.path).query).get('limit', 5)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(query_components)
    return
