#include <iostream>
#include <string>
#include "chassis.h"


class rover{

  public:
    void rover();
    void set_chassis(chassis);
    void test();


  private:
    chassis Chassis; //chassis de cada plataforma
    int hbridges;


}
