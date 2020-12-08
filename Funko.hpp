#include <iostream>
#include <stdlib.h>
using namespace std;
class Funko{
    protected:
        int *esquinas;
        string arch_audio;
        bool dentro;

        public:
            Funko(int x, int y, int ancho, int alto, string nuevo_arch_audio){
                esquinas=new int[4];
                esquinas[0]=x;
                esquinas[1]=y;
                esquinas[2]=x+ancho;
                esquinas[3]=y+alto;
                arch_audio=nuevo_arch_audio;
                dentro=false;
            }
            void checarMouse(int x, int y){
                if (x>=esquinas[0] && x<=esquinas[2] && y>=esquinas[1] && y<=esquinas[3]){
                    if (!dentro){
                        system("python reproducirSonido.py "+arch_audio);//reproducir sonido
                        dentro=true;
                    }
                }
                else{
                    dentro=false;
                }
            }
};