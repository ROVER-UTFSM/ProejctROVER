class vector2D{

  public:
    vector2D();
    float getVector();
    float operator+(float);
    float operator*(float);
    float operator/(float);
    float operator-(float);

  private:
    float pos_x;
    float pos_y;
    float speed_x;
    float speed_y;
    float acc_x;
    float acc_y;
};
