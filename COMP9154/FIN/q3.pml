bit lock = false;

inline enterM()
{
    atomic
    {
        enterI();
    }
}
inline leaveM()
{
    atomic
    {
        enterI();
    }
}
inline WaitM()
{
    atomic
    {
        enterI();
    }
}









proctype Q()
{
    do
    ::        lock = false;
    od;
}


init {run Q();}