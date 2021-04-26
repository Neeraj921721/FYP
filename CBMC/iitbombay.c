int foo(int a,int b , int c)
{
int d;
if (a > 12 && b < 45)
{
if (c > 4)
{
__CPROVER_assert(0,"ASSERTION VIOLATION");
d =1;
}
else
{
d = 2;
__CPROVER_assert(0,"ASSERTION VIOLATION");
}}
else
d = 3;
return d;
}
int main()
{
foo(13,5,6);
return 0;
}
