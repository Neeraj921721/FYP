/* Generated by CIL v. 1.3.7 */
/* print_CIL_Input is true */



typedef int bool;
typedef char msg_t;
typedef int port_t;
int kappa  =    0;
void assert(bool arg ) ;
msg_t nomsg  =    (char)-1;
char r1  ;
port_t p1  ;
char p1_old  ;
char p1_new  ;
char id1  ;
char st1  ;
msg_t send1  ;
bool mode1  ;
port_t p2  ;
char p2_old  ;
char p2_new  ;
char id2  ;
char st2  ;
msg_t send2  ;
bool mode2  ;
port_t p3  ;
char p3_old  ;
char p3_new  ;
char id3  ;
char st3  ;
msg_t send3  ;
bool mode3  ;
void node1(void) 
{ msg_t m1 ;

  {
  m1 = nomsg;
  if (mode1) {
    if ((int )r1 == 255) {
      r1 = (char)2;
    }
    r1 = (char )((int )r1 + 1);
    m1 = p3_old;
    p3_old = nomsg;
    if ((int )m1 != (int )nomsg) {
      if ((int )m1 > (int )id1) {
        send1 = m1;
      } else {
        if ((int )m1 == (int )id1) {
          st1 = (char)1;
        } else {
          send1 = m1;
        }
      }
    }
    mode1 = 0;
  } else {
    if ((int )send1 != (int )nomsg) {
      if ((int )p1_new == (int )nomsg) {
        p1_new = send1;
      } else {
        p1_new = p1_new;
      }
    } else {
      p1_new = p1_new;
    }
    mode1 = 1;
  }
  return;
}
}
void node2(void) 
{ msg_t m2 ;

  {
  m2 = nomsg;
  if (mode2) {
    m2 = p1_old;
    p1_old = nomsg;
    if ((int )m2 != (int )nomsg) {
      if ((int )m2 > (int )id2) {
        send2 = m2;
      } else {
        if ((int )m2 == (int )id2) {
          st2 = (char)1;
        }
      }
    }
    mode2 = 0;
  } else {
    if ((int )send2 != (int )nomsg) {
      if ((int )p2_new == (int )nomsg) {
        p2_new = send2;
      } else {
        p2_new = p2_new;
      }
    } else {
      p2_new = p2_new;
    }
    mode2 = 1;
  }
  return;
}
}
void node3(void) 
{ msg_t m3 ;

  {
  m3 = nomsg;
  if (mode3) {
    m3 = p2_old;
    p2_old = nomsg;
    if ((int )m3 != (int )nomsg) {
      if ((int )m3 > (int )id3) {
        send3 = m3;
      } else {
        if ((int )m3 == (int )id3) {
          st3 = (char)1;
        }
      }
    }
    mode3 = 0;
  } else {
    if ((int )send3 != (int )nomsg) {
      if ((int )p3_new == (int )nomsg) {
        p3_new = send3;
      } else {
        p3_new = p3_new;
      }
    } else {
      p3_new = p3_new;
    }
    mode3 = 1;
  }
  return;
}
}
int init(void) 
{ int tmp ;

  {
  if ((int )r1 == 0) {
    if ((int )id1 >= 0) {
      if ((int )st1 == 0) {
        if ((int )send1 == (int )id1) {
          if (mode1 == 0) {
            if ((int )id2 >= 0) {
              if ((int )st2 == 0) {
                if ((int )send2 == (int )id2) {
                  if (mode2 == 0) {
                    if ((int )id3 >= 0) {
                      if ((int )st3 == 0) {
                        if ((int )send3 == (int )id3) {
                          if (mode3 == 0) {
                            if ((int )id1 != (int )id2) {
                              if ((int )id1 != (int )id3) {
                                if ((int )id2 != (int )id3) {
                                  tmp = 1;
                                } else {
                                  tmp = 0;
                                }
                              } else {
                                tmp = 0;
                              }
                            } else {
                              tmp = 0;
                            }
                          } else {
                            tmp = 0;
                          }
                        } else {
                          tmp = 0;
                        }
                      } else {
                        tmp = 0;
                      }
                    } else {
                      tmp = 0;
                    }
                  } else {
                    tmp = 0;
                  }
                } else {
                  tmp = 0;
                }
              } else {
                tmp = 0;
              }
            } else {
              tmp = 0;
            }
          } else {
            tmp = 0;
          }
        } else {
          tmp = 0;
        }
      } else {
        tmp = 0;
      }
    } else {
      tmp = 0;
    }
  } else {
    tmp = 0;
  }
  return (tmp);
}
}
int check(void) 
{ int tmp ;

  {
  if (((int )st1 + (int )st2) + (int )st3 <= 1) {
    if ((int )r1 >= 3) {
      goto _L;
    } else {
      if (((int )st1 + (int )st2) + (int )st3 == 0) {
        _L: 
        if ((int )r1 < 3) {
          tmp = 1;
        } else {
          if (((int )st1 + (int )st2) + (int )st3 == 1) {
            tmp = 1;
          } else {
            tmp = 0;
          }
        }
      } else {
        tmp = 0;
      }
    }
  } else {
    tmp = 0;
  }
  return (tmp);
}
}

void sanghu(bool arg ) 
{ 

  {
  if (! arg) {
    printf("");
  }
  return;
}
}

int main(void) 
{ int c1 ;
  int i2 ;

  {
  c1 = 0;
  klee_make_symbolic(& r1, sizeof(char ), "r1");
  klee_make_symbolic(& id1, sizeof(char ), "id1");
  klee_make_symbolic(& st1, sizeof(char ), "st1");
  klee_make_symbolic(& send1, sizeof(char ), "send1");
  klee_make_symbolic(& mode1, sizeof(bool ), "mode1");
  klee_make_symbolic(& id2, sizeof(char ), "id2");
  klee_make_symbolic(& st2, sizeof(char ), "st2");
  klee_make_symbolic(& send2, sizeof(char ), "send2");
  klee_make_symbolic(& mode2, sizeof(bool ), "mode2");
  klee_make_symbolic(& id3, sizeof(char ), "id3");
  klee_make_symbolic(& st3, sizeof(char ), "st3");
  klee_make_symbolic(& send3, sizeof(char ), "send3");
  klee_make_symbolic(& mode3, sizeof(bool ), "mode3");
  i2 = init();
  p1_old = nomsg;
  p1_new = nomsg;
  p2_old = nomsg;
  p2_new = nomsg;
  p3_old = nomsg;
  p3_new = nomsg;
  i2 = 0;
  while (i2 < 2) {
    node1();
    node2();
    node3();
    p1_old = p1_new;
    p1_new = nomsg;
    p2_old = p2_new;
    p2_new = nomsg;
    p3_old = p3_new;
    p3_new = nomsg;
    c1 = check();
    sanghu(c1);
    i2 = i2 + 1;
  }
/*  _SLICE(kappa);*/
  return (0);
}
}
