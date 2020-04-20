import argparse
import requests
import json
import os

target= ''

ap = argparse.ArgumentParser(description='develop and testing tools')
ap.add_argument('-e', '--env', required=True, choices=['dev', 'stg', 'aws-stg', 'aws-prd'], help='target env')
ap.add_argument('-c', '--cmd', required=True, choices=['addBill', 'removeMeter', 'mslog', 'dsclog', 'icicis', 'icicir'], help='command')
ap.add_argument('-d', '--date', required=False, help='date, [mslog, dsclog, icicis] support this arg')
ap.add_argument('-f', '--force', required=False, help='force add bill, "addBill" support this arg')
ap.add_argument('-p', '--payload', required=False, help='obj to update to database, should be a JSON boj string, [addBill, icicir] support this arg')
ap.add_argument('-i', '--id', required=False, help='id of database item, should be a string, "removeMeter" support this arg')
ap.add_argument('-o', '--output', required=False, help='path to save download file, [mslog, dsclog, icicis] support this arg')
args = vars(ap.parse_args())
# print(args)

class ArgumentError(Exception):
  """argument not correct"""
  pass

class OptBase:
  path=''
  data={}
  def __init__(self, args):
    self.data={
      'env':args['env']
    }
  def success(self, res):
    print('done')

  def run(self):
    try:
      res = requests.post(target+self.path, data=self.data)
      if res.status_code == 200:
        self.success(res)
      else:
        print(res.text)
    except Exception as e:
      print(e)

class AddBill(OptBase):
  def __init__(self, args):
    super().__init__(args)
    self.path='/db/createbill'
    if not args['payload']:
      raise ArgumentError
    self.data['bill']= args['payload']
    self.data['force']= args['force']

class RemoveMeter(OptBase):
  def __init__(self, args):
    super().__init__(args)
    self.path='/db/removeMeter'
    self.data['meterID']= args['id']

  def success(self, res):
    result = json.loads(res.text)
    if result['nRemoved'] == 0:
      print('Can\'t find meter:', args['id'])
    else:
      super().success(res)

class ICICIR(OptBase):
  def __init__(self, args):
    super().__init__(args)
    self.path='/upload/icici/report'
    if not args['payload']:
      raise ArgumentError
    self.data['report']= args['payload']

class Download(OptBase):
  def __init__(self, args):
    super().__init__(args)
    self.data['date']= args['date']

  def success(self, res):
    fname = res.headers['x-filename']
    if args['output']:
      lpath, lfile = os.path.split(args['output'])
      if lpath and not os.path.isdir(lpath):
        os.mkdir(lpath)
      if(not lfile):
        fname = os.path.join(args['output'], fname)
      else:
        fname = os.path.abspath(args['output'])
    else:
      fname = os.path.abspath(fname)
    try:
      with open(fname, 'wb') as f:
        f.write(res.content)
        print('download file: '+fname)
    except FileNotFoundError as e:
      print(e)


class Mslog(Download):
  def __init__(self, args):
    super().__init__(args)
    self.path='/download/mslog'

class Dsclog(Download):
  def __init__(self, args):
    super().__init__(args)
    self.path='/download/dsclog'

class ICICIS(Download):
  def __init__(self, args):
    super().__init__(args)
    self.path='/download/icici/statement'

try:
  builder={
    'mslog': Mslog,
    'dsclog': Dsclog,
    'icicis': ICICIS,
    'icicir': ICICIR,
    'addBill': AddBill,
    'removeMeter': RemoveMeter
  }
  runner = builder[args['cmd']](args)
  runner.run()
except KeyError:
  print('command:', args['cmd'], 'not support!')
except ArgumentError:
  print('argument not correct')
except Exception as e:
  print('Unexpect Error: ', e)
