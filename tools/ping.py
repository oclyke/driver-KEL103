#!/usr/bin/env python3

# uses parallel subprocesses to ping a range of ip addresses and list which responded

import argparse
import subprocess

def main(args):

  # comprehend a string as a csv list of ranges
  def str2range(s):
    return sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))])) if '-' in i else [int(i)]) for i in s.split(',')), [])

  active = []
  processes = []

  # determine network id minus host id
  sep = '.'
  network_id = sep.join(args.network.split(sep, 3)[:3] + [''])

  # sort and remove duplicate host ids using set()
  host_ids = set(str2range(args.hosts)) 

  # start subprocesses to ping each network_id + host_id combination
  for id in host_ids:
    addr = network_id + str(id)
    p = subprocess.Popen(['ping', '-c', '1', '-W', '1', addr], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    processes.append((p, addr))

  # wait for results
  for p, addr in processes:
    p.wait()
    if p.returncode == 0:
      active.append(addr)

  # print results
  print('devices found at: ')
  for addr in active:
    print(addr)

# when run as the main script:
if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Parallel Network Ping Utility')

  parser.add_argument('network', help='the ipv4 address specifying the network id. host id is ignored an replaced by the \'host\' range argument.')
  parser.add_argument('--hosts', dest='hosts', required=False, default='0-255', 
                        help='range of host ids to check. \
                              comma separated list of ranges \'a-b\' or simply \'c\'.\
                              range pairs must be sorted low-high.\
                              range pairs may appear in any order in the list.\
                              use quotes if spaces included in the list.\
                              example: \'e-f,a, b, g, k-p, c, z\'\
                              '
                      )

  args = parser.parse_args()
  main(args)
