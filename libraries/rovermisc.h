#ifndef __ROVERMISC_H_
#define __ROVERMISC_H_


#ifdef __linux__	// ############ LINUX ##############

#include <time.h>

namespace rover{

	int wait(unsigned int useconds);

}

#endif				// ########### LINUX ##############



#ifdef __MINGW32__
#endif // __MINGW32__



#endif // __ROVERMISC_H_
