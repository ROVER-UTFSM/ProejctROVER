#include <iostream>
#include <string>
#include "chassis.h"


#include "chassis.h"
#include "arduino.h"

namespace rover{

    class rover{
    public:
        rover(){}
        ~rover(){}

        void test();

    private:
    	chassis Chassis;
    	arduino Arduino;
    };

}
