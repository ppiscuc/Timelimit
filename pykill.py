#!/usr/bin/env python

import subprocess
import time


def runCommand(cmd,inputData,timeout = 2):
    """
    Ruleaza comanda, si ii trimite un -9 daca dureaza prea mult
    """
    q = subprocess.Popen(['echo',inputData], stdout = subprocess.PIPE)
    p = subprocess.Popen(cmd,env={"PATH":"/tmp"},stdin = q.stdout, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = False)

    t_start = time.time()
    seconds_passed  = 0

    out = ''

    while p.poll() is None and seconds_passed < timeout:
        time.sleep(0.1) # dormi putin
        seconds_passed = time.time() - t_start
        print ("passed: %s" % seconds_passed)

    if seconds_passed >= timeout:
        try:
            p.stdout.close()
            p.stderr.close()
            p.terminate()
        except:
            pass
        finally:
            return (0,(0,0))
    returncode = p.returncode
    out = p.communicate()

    return(returncode, out)

if __name__ == '__main__':
    data = ''
    print runCommand("./a.out",data)
