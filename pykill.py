#!/usr/bin/env python

import subprocess
import time


def runCommand(cmd,timeout = 2):
    """
    Ruleaza comanda, si ii trimite un -9 daca dureaza prea mult
    """
    q = subprocess.Popen(['echo','bla bla'], stdout = subprocess.PIPE)
    p = subprocess.Popen(cmd,stdin = q.stdout, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = False)
    #p = subprocess.Popen(cmd,stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = False)

    t_start = time.time()
    seconds_passed  = 0

    out = ''

    while p.poll() is None and seconds_passed < timeout:
        time.sleep(0.1) # dormi putin
        seconds_passed = time.time() - t_start
        print ("passed: %s" % seconds_passed)

    print("am ajuns aici")
    if seconds_passed >= timeout:
        try:
            print("trebuie sa inchid chestii")
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
def run(cmd):
    """
    Ruleaza comanda, cu input, si ii trimite un -9 daca dureaza prea mult
    """
    exec_proc = subprocess.Popen("./a.out",stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = False)
    max_time = 1
    cur_time = 0.0
    return_code = 0

    while cur_time <= max_time:
        if exec_proc.poll() != None:
            return_code = exec_proc.poll()
            break
        time.sleep(0.1)
        cur_time += 0.1
    if cur_time > max_time:
        exec_proc.kill()
        return "Killed"
    if exec_proc.poll() == None:
        return "0"

if __name__ == '__main__':
    print runCommand("./a.out")

