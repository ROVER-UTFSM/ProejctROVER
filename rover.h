#include <iostream>
#include <string>

#include "chassis.h"
#include "arduino.h"

class rover{

public:
    std::string type;
    
    void set_type(std::string);

    void test();

private:
	chassis Chassis;
	arduino Arduino;
};
