Exceptions
-------------
Syntax is correct but errors occurs are run/execution time

Normal Flow VS Exception Flow
Normal Flow: Successful execution of work
e.g.: using ATM transaction(withdraw)
withdraw amount > balance (throw an error)
daily limit
machine do not have sufficient amount

Exception classes
--------------------------
    1: Default Except Mechanism(python) DFM => predefined Exception
    2: User Defined Mechanism (Dev) UDM => user defined Exception
 
NOTE: IF DFM will run program will be terminated at that steps

 Raise     |   Handle
 _________    _________
 1. python         DEM
 2. python         UDEM(user/dev )
 3. user           DEM
 4. user           UDEM
 ------------------------------------------
 keyword used in Exception handling
  try
  catch
  finally
  raise (used in 3, 4)
  
 -------------------------------------------------
1: write code in try block if there is any possibility of exception
2: no except without try
3: raised exception should be handled by same type of class e.g.: ZeroDivisionError
4: no exception raised in try, then except block is skipped
5: multiple except block in one try block (multiple type exception can occur in try block)
6: DEM will run if exception class does not matched with raised exception class
7: finally runs always (DEM calls finally before termination)
8: te, ef, tef, teef,..
    try
    --
    except (0 or more)
    ----
    finally (0 or 1)
9: two are  more exception class in same except
10: default excption: do not mention any exception class name
11: else: It will run if no exception raised in try block

Note: user means developer :P

raise exception from user(developer)
------------------------------------
we can create our own exception class or use standard exception class

 
 
 
 
    
