
	# Данные задачи
a = 1.42
b = -2.73
c = 2.19
d = 1.86
k=6
t1 = 0.95
	#Тестовые данные
a = 1.5
b = -3
c = 2.30
d = 2
k=4
t1 = 1.2

Trajectory (t1)
Console.WriteLine(" Коорднината x1= {0:F5}",x(t1))
Console.WriteLine (" Коорднината yl={0:F5}",y(t1))

Console.WriteLine (" Составляющая Vx={0:F5}",Vx(t1))
Console.WriteLine (" Составляющая Vy={0:F5}",Vy(t1))
Console.WriteLine(" Модуль скорости V={0:F5}",V(t1))

Console.WriteLine (" Составляющая Wx={0:F5}",Wx(t1))
Console.WriteLine (" Составляющая Wy={0:F5}",Wy(t1))
Console.WriteLine(" Модуль скорости W={0:F5}",W(t1))

Console.WriteLine (" Составляющая Wt={0:F5}",Wt(t1))
Console.WriteLine (" Составляющая Wn={0:F5}",Wn(t1))
Console.WriteLine(" Радиус кривизны ro={0:F5}",ro(t1))
Trajectory(t1,5)
Draw_VxVy(t1,3)
Draw_WxWyWtWn(t1,1.5)

def Vx(t):
	return -Math.PI*b*Math.Sin(Math.PI*t/k)/k

	static double Vy(double t)
	{
		return d*Math.PI*Math.Cos(Math.PI*t/k)/k;
	}
	static double V(double t)
	{
		return Math. Sqrt (Vx (t) * Vx(t) + Vy(t) * Vy(t));
	}
	static double Wx(double t){
		return -(Math.PI*Math.PI/(k*k))*b*Math.Cos(Math.PI*t/k);
	}
	static double Wy(double t){
		return -(Math.PI*Math.PI/(k*k))*d*Math.Sin(Math.PI*t/k);
	}
	static double W(double t){
		return Math. Sqrt (Wx (t) * Wx(t) + Wy(t) * Wy(t));
	}

	static double Wt(double t){
		return ((Vx(t) * Wx(t) + Vy(t) * Wy(t)) / V(t));
	}
	static double Wn(double t){
		return Math.Sqrt (W(t) * W(t) - Wt(t) * Wt(t));
	}
	static double ro(double t){
		return V(t) * V(t) / Wn(t);
	}

	static void Trajectory(double t)
	{
		int n = 20; string frmt = " ti = {0:F3} xi = {1:F5} yi = {2:F5}";
		double to = 0.5 *t, tn =1.5 * t, ht = (tn - to) / n, ti;
		for (int i = 0; i <= n; i++)
		{
			ti= to +i * ht; Console.WriteLine(frmt, ti, x(ti), y(ti));
		}
	}

	static void Trajectory(double t, double m)
	{
		int n = 20;
		double to = 0.5 * t, tn = 1.5 * t, ht = (tn - to) / n, ti;
		string frmt =" ti = {0:F3} xi = {1:F1} yi = {2:F1}";
		double min_x = double.MaxValue, max_x = double. MinValue;
		double min_y = double. MaxValue, max_y = double. MinValue;
		for (int i=0; i <= n; i++)
		{
			ti=to+i* ht;
			min_x = Math.Min(min_x, x(ti)); max_x = Math.Max(max_x, x(ti));
			min_y = Math.Min(min_y, y(ti)); max_y = Math.Max(max_y, y(ti));
		}
		double mash = m / Math.Min((max_x - min_x), (max_y - min_y));
		Console. WriteLine ("\r\nТраектория в масштабе");
		for (int i = 0; i <= n; i++)
		{
			ti=to+i* ht;
			Console.WriteLine(frmt, ti, x(ti) * mash, y(ti) * mash);
		}
	}
	static void Draw_VxVy(double t, double m){
		double mash = m / Math.Min(Math.Abs(Vx(t)), Math.Abs(Vy(t)));
		Console.WriteLine (" Составляющая Vx={0:F5} см. в масштабе",Vx(t1)*mash);
		Console.WriteLine (" Составляющая Vy={0:F5} см. в масштабе",Vy(t1)*mash);
	}

	static void Draw_WxWyWtWn(double t, double m){
		double mash = m / Math.Min(Math.Min(Math.Abs(Wx(t)), Math.Abs(Wy(t))),Math.Min(Math.Abs(Wt(t)),Math.Abs(Wn(t))));
		Console.WriteLine (" Составляющая Wx={0:F5} см. в масштабе",Wx(t1)*mash);
		Console.WriteLine (" Составляющая Wy={0:F5} см. в масштабе",Wy(t1)*mash);
		Console.WriteLine (" Составляющая Wt={0:F5} см. в масштабе ",Wt(t1)*mash);
		Console.WriteLine (" Составляющая Wn={0:F5} см. в масштабе",Wn(t1)*mash);
	}
	static double x (double t){
		return a+b*Math.Cos(Math.PI*t/k);
	}

	static double y(double t)
	{
		return c+d*Math.Sin(Math.PI*t/k);
	}
}
