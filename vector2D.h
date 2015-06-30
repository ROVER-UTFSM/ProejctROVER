namespace rover{


    // Describe un vector cartesiano y sobrecarga operadores
    class vector2D_t{
    private:
        float x;
        float y;

    public:
        vector2D_t(){
            vector_t(0.,0.);
        }
        vector2D_t(float xp, float yp): x(xp), y(yp){}
        ~vector2D_t(){}

        vector2D_t operator=(vector_t2D v);
        vector2D_t operator+(vector_t2D v);
        vector2D_t operator-(vector_t2D v);
        vector2D_t operator*(float);
        vector2D_t operator/(float);
    };

    // Usa vector_t para describir posicion, velocidad y aceleracion
    class state_vector2D{
    private:
        vector2D_t pos;
        vector2D_t spd;
        vector2D_t acc;
    
    public:
        state_vector2D();
        ~state_vector2D();
        
        state_vector2D operator=(state_vector2D v);
        state_vector2D operator+(state_vector2D v);
        state_vector2D operator-(state_vector2D v);
        state_vector2D operator*(float);
        state_vector2D operator/(float);

    };    

}
