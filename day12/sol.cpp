#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cassert>
#include <xmmintrin.h>

using namespace std;

typedef unsigned long long ull;
typedef int int4 __attribute__ ((vector_size (4 * sizeof(int))));

static int4* int4_alloc(std::size_t n) {
    void* tmp = 0;
    if (posix_memalign(&tmp, sizeof(int4), sizeof(int4) * n)) {
        throw std::bad_alloc();
    }
    return (int4*)tmp;
}

inline int4 sign(int4 b, int4 a) {
    return (a < b) - (b < a);
}

ull repeats_at(int n, int r, int4* moon_pos, int4* orig_pos, int4* moon_vel) {
    for(int i=0;i<n;i++) {
        moon_pos[i] = orig_pos[i];

        int4 zero = {0, 0, 0, 0};
        moon_vel[i] = zero;
    }

    ull step = 0;
    while(true) {
        step++;

        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                moon_vel[i] += sign(moon_pos[i], moon_pos[j]);
            }
        }

        for(int i=0;i<n;i++) {
            moon_pos[i] += moon_vel[i];
        }

        bool good = true;
        for(int k=0;k<n;k++) {
            if(moon_pos[k][r] != orig_pos[k][r] || moon_vel[k][r]) {
                good = false;
                break;
            }
        }

        if(good) {
            return step;
        }
    }
}

int main() {
    int4* moon_pos = int4_alloc(5);
    int4* orig_pos = int4_alloc(5);
    int4* moon_vel = int4_alloc(5);

    std::ifstream infile("input");

    int n = 0;
    int4 pos_sum = {0, 0, 0, 0};

    std::string line;
    while (std::getline(infile, line))
    {
        std::istringstream iss(line);
        char _; int x, y, z;
        iss >> _ >> _ >> _ >> x >> _ >> _ >> _ >> y >> _ >> _ >> _ >> z;

        int4 pos = {x, y, z, 0};
        int4 vel = {0, 0, 0, 0};

        moon_pos[n] = pos;
        orig_pos[n] = pos;
        moon_vel[n] = vel;

        pos_sum += pos;

        n++;
    }

    for(int i=0;i<3;i++)
        cout << repeats_at(n, i, moon_pos, orig_pos, moon_vel) << endl;

    return 0;
}