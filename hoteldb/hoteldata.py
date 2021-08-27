#CREATING THE DATABASE
import sqlite3
conn=sqlite3.connect('bentley.db')
c=conn.cursor()
c.executescript(
    '''
      create table customer( id NUMBER(6) PRIMARY KEY,
                             name TEXT,
                             age NUMBER,
                             member TEXT ,
                             phone TEXT UNIQUE,
                             CHECK(age>=18 AND length(phone)==10
                                   AND member IN('S','V','P') AND length(name)>0)
                           );
                           
      create table staff( id NUMBER(4) PRIMARY KEY,
                          name TEXT,
                          age NUMBER,
                          salary NUMBER(6,2),
                          phone TEXT UNIQUE,
                          CHECK(age>=18 AND length(phone)==10
                                AND length(name)>0)
                        );
        
      create table restaurant( id NUMBER(3) PRIMARY KEY,
                               name TEXT UNIQUE,
                               type TEXT,
                               price NUMBER(4,2),
                               CHECK(type in('F','B'))
                             );
                             
      insert into customer values(100001,'KL RAHUL',27,'P','9999999999');
      insert into customer values(100002,'NEIL WAGNER',36,'S','9999999988');
      insert into customer values(100003,'DAVID WARNER',54,'V','9999999888');
      insert into customer values(100004,'STEVE SMITH',33,'P','9999998888');
      insert into customer values(100005,'VIRAT KOHLI',43,'P','9999988888');
      insert into customer values(100006,'BADRINATH',24,'P','9999888888');
      insert into customer values(100007,'PRAVEEN',19,'S','9998888888');
      insert into customer values(100008,'NAVEEN',45,'S','9988888888');
      insert into customer values(100009,'RAMESH',59,'V','9888888888');
      insert into customer values(100010,'MUKIL',61,'V','8888888888');
      insert into customer values(100011,'WATSON',43,'S','9999999997');
      insert into customer values(100012,'SURESH',32,'P','9999999977');
      insert into customer values(100013,'STALIN',29,'V','9999999777');
      insert into customer values(100014,'BABUR',39,'P','9999997777');
      insert into customer values(100015,'STOKES',30,'V','9999977777');
      insert into customer values(100016,'ROHIT SHARMA',47,'P','9999777777');
      insert into customer values(100017,'ASHWIN',23,'S','9997777777');
      insert into customer values(100018,'MANDANA',29,'S','9977777777');
      insert into customer values(100019,'TZUYU',20,'S','9777777777');
      insert into customer values(100020,'ALIA',28,'V','7777777777');
      insert into customer values(100021,'DRAVID',43,'V','9999999996');
      insert into customer values(100022,'DEEPIKA',34,'P','9999999966');
      insert into customer values(100023,'SRUTHI',38,'P','9999999666');
      insert into customer values(100024,'ABRAHAM BENJAMIN',40,'V','9999996666');
      insert into customer values(100025,'SHRAYANTHI',25,'S','9999966666');
      insert into customer values(100026,'SAMANTHA',28,'P','9999666666');
      insert into customer values(100027,'VIJAY',44,'S','9996666666');
      insert into customer values(100028,'LAKSHMI',54,'V','9966666666');
      insert into customer values(100029,'POOJA',37,'P','9666666666');
      insert into customer values(100030,'PALANISWAMY',62,'S','6666666666');
      insert into customer values(100031,'CUMMINS',26,'P','9876543210');
      insert into customer values(100032,'SUNDOG',21,'P','7010015050');
      insert into customer values(100033,'BALASUBRAMANIAN',60,'S','9486103109');
      insert into customer values(100034,'ELLYSE PERRY',31,'S','9999999995');
      insert into customer values(100035,'KARUN',22,'P','9999999955');
      insert into customer values(100036,'HARI',37,'S','9999999555');
      insert into customer values(100037,'ANISH',43,'V','9999995555');
      insert into customer values(100038,'VIJAY',19,'V','9999955555');
      insert into customer values(100039,'AADITHYA',22,'V','9999555555');
      insert into customer values(100040,'VIGNESH',53,'V','9995555555');
      insert into customer values(100041,'ABIJITH',29,'S','9955555555');
      insert into customer values(100042,'ASHWIN',36,'P','9555555555');
      insert into customer values(100043,'SRIVATHSAV',25,'S','9962275888');
      insert into customer values(100044,'PARTHEBAN',49,'P','6383763258');
      insert into customer values(100045,'JIMMY ANDERSON',41,'P','6767676767');
      insert into customer values(100046,'MS DHONI',40,'S','7676767676');
      insert into customer values(100047,'WARNE',51,'S','6481801123');
      insert into customer values(100048,'INDIRA',31,'V','6899866900');
      insert into customer values(100049,'MOUNT BATTEN',65,'V','9876567896');
      insert into customer values(100050,'RAJINI',77,'V','9940334184');
      insert into customer values(100051,'AJITH',87,'P','9333333330');
      insert into customer values(100052,'VIVEK',59,'S','9000000000');
      
      insert into staff values(1001,20,'MONIESH',500000,'6381801176');
      insert into staff values(1002,32,'NIRMALA',250000,'7381801176');
      insert into staff values(1003,43,'VELUMANI',250000,'8381801176');
      insert into staff values(1004,45,'HARIHARAN',200000,'9381801176');
      insert into staff values(1005,51,'RAVICHANDRAN',200000,'6581801176');
      insert into staff values(1007,34,'RAHUL KRISHNA',200000,'6681801176');
      insert into staff values(1008,36,'BHUVANESHWAR KUMAR',200000,'6781801176');
      insert into staff values(1009,28,'JAYA',100000,'6881801176');
      insert into staff values(1010,29,'RAMACHANDRAN',100000,'6981801176');
      insert into staff values(1011,21,'NARENDRA MODI',100000,'6391801176');
      insert into staff values(1012,36,'LIONEL MESSI',100000,'6371801176');
      insert into staff values(1013,38,'PEINALDO',75000,'6361801176');
      insert into staff values(1014,39,'NEYMAR',75000,'6351801176');
      insert into staff values(1015,42,'TSITIPAS',50000,'6341801176');
      insert into staff values(1016,45,'DEVI',50000,'6331801176');
      insert into staff values(1017,32,'BILLY BOWDEN',50000,'6321801176');
      insert into staff values(1018,33,'UGESH',50000,'6311801176');
      insert into staff values(1019,31,'KAILSAH',30000,'6389801176');
      insert into staff values(1020,44,'ABINAYA',30000,'6388801176');
      insert into staff values(1021,23,'VASUKI',20000,'6387801176');
      insert into staff values(1022,47,'SITA',25000,'6386801176');
      insert into staff values(1023,49,'RAM',25000,'6385801176');
      insert into staff values(1024,55,'SHANKAR',20000,'6384801176');
      insert into staff values(1025,19,'KALYANI',15000,'6383801176');
      insert into staff values(1026,36,'KAMATCHI',10000,'6382801176');
      
      insert into restaurant values(101,'DOSA','F',100);
      insert into restaurant values(102,'IDLI','F',70);
      insert into restaurant values(103,'MASAL DOSA','F',120);
      insert into restaurant values(104,'CHAPPATHI','F',80);
      insert into restaurant values(105,'PAROTTA','F',100);
      insert into restaurant values(106,'POORI','F',70);
      insert into restaurant values(107,'PANNER BUTTER MASALA','F',250);
      insert into restaurant values(108,'CHOLA POORI','F',120);
      insert into restaurant values(109,'GOBI 65','F',200);
      insert into restaurant values(110,'VEG SANDWICH','F',80);
      insert into restaurant values(111,'CHICKEN SANDWICH','F',90);
      insert into restaurant values(112,'VEG MEALS','F',200);
      insert into restaurant values(113,'NON-VEG MEALS','F',230);
      insert into restaurant values(114,'VEG FRIED RICE','F',200);
      insert into restaurant values(115,'CHICKEN FRIED RICE','F',220);
      insert into restaurant values(116,'CHICKEN LOLIPOP','F',200);
      insert into restaurant values(117,'CHICKEN 65','F',250);
      insert into restaurant values(118,'VADA','F',50);
      insert into restaurant values(119,'NAAN','F',70);
      insert into restaurant values(120,'ICE-CREAM','F',50);
      insert into restaurant values(121,'GOBI MANCHURIAN','F',250);
      insert into restaurant values(122,'NOODLES','F',100);
      insert into restaurant values(123,'PASTA','F',80);
      insert into restaurant values(124,'PIZZA','F',300);
      insert into restaurant values(125,'WATER BOTTLE','B',100);
      insert into restaurant values(126,'COFFEE','B',120);
      insert into restaurant values(127,'TEA','B',120);
      insert into restaurant values(128,'LEMONADE','B',150);
      insert into restaurant values(129,'OLD MONK','B',200);
      insert into restaurant values(130,'ROYAL CHALLENGE','B',230);
      insert into restaurant values(131,'BIRA 91','B',250);
      insert into restaurant values(132,'OFFICERS CHOICE','B',225);
      insert into restaurant values(133,'MCDOWELLS','B',300);
      insert into restaurant values(134,'BLENDERS','B',350);
    '''
)
conn.commit()
conn.close()
