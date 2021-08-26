#CREATING THE DATABASE
import sqlite3
conn=sqlite3.connect('bentley.db')
c=conn.cursor()
c.executescript(
    '''
      create table customer( id TEXT PRIMARY KEY,
                             name TEXT,
                             age NUMBER,
                             phone TEXT UNIQUE
                           );
                           
      create table staff( id TEXT PRIMARY KEY,
                          name TEXT,
                          age NUMBER,
                          salary NUMBER(6,2),
                          phone TEXT UNIQUE
                        );
        
      create table restaurant( id TEXT PRIMARY KEY,
                               name TEXT,
                               price NUMBER(4,2)
                             );
                             
      insert into customer values('PCS0001','KL RAHUL',27,'9999999999');
      insert into customer values('SCS0901','NEIL WAGNER',36,'9999999988');
      insert into customer values('PCS0801','DAVID WARNER',54,'9999999888');
      insert into customer values('PCS2201','STEVE SMITH',33,'9999998888');
      insert into customer values('VCS1801','VIRAT KOHLI',43,'9999988888');
      insert into customer values('VCS0891','BADRINATH',24,'9999888888');
      insert into customer values('VCS9901','PRAVEEN',19,'9998888888');
      insert into customer values('SCS6701','NAVEEN',45,'9988888888');
      insert into customer values('SCS9999','RAMESH',59,'9888888888');
      insert into customer values('VCS0802','MUKIL',61,'8888888888');
      insert into customer values('PCS0804','WATSON',43,'9999999997');
      insert into customer values('PCS0802','SURESH',32,'9999999977');
      insert into customer values('PCS1111','STALIN',29,'9999999777');
      insert into customer values('SCS1234','BABUR',39,'9999997777');
      insert into customer values('PCS2345','STOKES',30,'9999977777');
      insert into customer values('VCS3456','ROHIT SHARMA',47,'9999777777');
      insert into customer values('VCS4567','ASHWIN',23,'9997777777');
      insert into customer values('SCS5678','MANDANA',29,'9977777777');
      insert into customer values('SCS6789','TZUYU',20,'9777777777');
      insert into customer values('PCS6666','ALIA',28,'7777777777');
      insert into customer values('PCS7777','DRAVID',43,'9999999996');
      insert into customer values('SCS8888','DEEPIKA',34,'9999999966');
      insert into customer values('SCS1111','SRUTHI',38,'9999999666');
      insert into customer values('VCS2222','ABRAHAM BENJAMIN',40,'9999996666');
      insert into customer values('VCS3333','SHRAYANTHI',25,'9999966666');
      insert into customer values('VCS4444','SAMANTHA',28,'9999666666');
      insert into customer values('SCS5555','VIJAY',44,'9996666666');
      insert into customer values('SCS9876','LAKSHMI',54,'9966666666');
      insert into customer values('PCS8765','POOJA',37,'9666666666');
      insert into customer values('PCS7654','PALANISWAMY',62,'6666666666');
      insert into customer values('PCS6543','CUMMINS',26,'9876543210');
      insert into customer values('SCS5432','SUNDOG',21,'7010015050');
      insert into customer values('SCS4321','BALASUBRAMANIAN',60,'9486103109');
      insert into customer values('SCS1357','ELLYSE PERRY',31,'9999999995');
      insert into customer values('VCS3579','KARUN',22,'9999999955');
      insert into customer values('VCS5793','HARI',37,'9999999555');
      insert into customer values('VCS5973','ANISH',43,'9999995555');
      insert into customer values('VCS9753','VIJAY',19,'9999955555');
      insert into customer values('VCS9573','AADITHYA',22,'9999555555');
      insert into customer values('VCS9675','VIGNESH',53,'9995555555');
      insert into customer values('SCS9673','ABIJITH',29,'9955555555');
      insert into customer values('PCS9888','ASHWIN',36,'9555555555');
      insert into customer values('PCS9889','SRIVATHSAV',25,'9962275888');
      insert into customer values('PCS4563','PARTHEBAN',49,'6383763258');
      insert into customer values('PCS3425','JIMMY ANDERSON',41,'6767676767');
      insert into customer values('PCS4841','MS DHONI',40,'7676767676');
      insert into customer values('PCS1225','WARNE',51,'6481801123');
      insert into customer values('SCS1335','INDIRA',31,'6899866900');
      insert into customer values('VCS1445','MOUNT BATTEN',65,'9876567896');
      insert into customer values('PCS6225','RAJINI',77,'9940334184');
      insert into customer values('PCS8955','AJITH',87,'9333333330');
      insert into customer values('VCS5665','VIVEK',59,'9000000000');
      
      insert into staff values('CEO1',20,'MONIESH',500000,'6381801176');
      insert into staff values('M001',32,'NIRMALA',250000,'7381801176');
      insert into staff values('M003',43,'VELUMANI',250000,'8381801176');
      insert into staff values('C004',45,'HARIHARAN',200000,'9381801176');
      insert into staff values('C005',51,'RAVICHANDRAN',200000,'6581801176');
      insert into staff values('C006',34,'RAHUL KRISHNA',200000,'6681801176');
      insert into staff values('C007',36,'BHUVANESHWAR KUMAR',200000,'6781801176');
      insert into staff values('C008',28,'JAYA',100000,'6881801176');
      insert into staff values('CH09',29,'RAMACHANDRAN',100000,'6981801176');
      insert into staff values('CH10',21,'NARENDRA MODI',100000,'6391801176');
      insert into staff values('CH11',36,'LIONEL MESSI',100000,'6371801176');
      insert into staff values('RS12',38,'PEINALDO',75000,'6361801176');
      insert into staff values('RS13',39,'NEYMAR',75000,'6351801176');
      insert into staff values('RS14',42,'TSITIPAS',50000,'6341801176');
      insert into staff values('RS15',45,'DEVI',50000,'6331801176');
      insert into staff values('S016',32,'BILLY BOWDEN',50000,'6321801176');
      insert into staff values('S017',33,'UGESH',50000,'6311801176');
      insert into staff values('S018',31,'KAILSAH',30000,'6389801176');
      insert into staff values('S019',44,'ABINAYA',30000,'6388801176');
      insert into staff values('S020',23,'VASUKI',20000,'6387801176');
      insert into staff values('S021',47,'SITA',25000,'6386801176');
      insert into staff values('WA22',49,'RAM',25000,'6385801176');
      insert into staff values('WA23',55,'SHANKAR',20000,'6384801176');
      insert into staff values('AC24',19,'KALYANI',15000,'6383801176');
      insert into staff values('AC25',36,'KAMATCHI',10000,'6382801176');
      
      insert into restaurant values('F001','DOSA',100);
      insert into restaurant values('F002','IDLI',70);
      insert into restaurant values('F003','MASAL DOSA',120);
      insert into restaurant values('F004','CHAPPATHI',80);
      insert into restaurant values('F005','PAROTTA',100);
      insert into restaurant values('F006','POORI',70);
      insert into restaurant values('F007','PANNER BUTTER MASALA',250);
      insert into restaurant values('F008','CHOLA POORI',120);
      insert into restaurant values('F009','GOBI 65',200);
      insert into restaurant values('F011','VEG SANDWICH',80);
      insert into restaurant values('F012','CHICKEN SANDWICH',90);
      insert into restaurant values('F013','VEG MEALS',200);
      insert into restaurant values('F014','NON-VEG MEALS',230);
      insert into restaurant values('F015','VEG FRIED RICE',200);
      insert into restaurant values('F016','CHICKEN FRIED RICE',220);
      insert into restaurant values('F017','CHICKEN LOLIPOP',200);
      insert into restaurant values('F018','CHICKEN 65',250);
      insert into restaurant values('F019','VADA',50);
      insert into restaurant values('F020','NAAN',70);
      insert into restaurant values('F021','ICE-CREAM',50);
      insert into restaurant values('F022','GOBI MANCHURIAN',250);
      insert into restaurant values('F023','NOODLES',100);
      insert into restaurant values('F024','PASTA',80);
      insert into restaurant values('F025','PIZZA',300);
      insert into restaurant values('B001','WATER BOTTLE',100);
      insert into restaurant values('B002','COFFEE',120);
      insert into restaurant values('B003','TEA',120);
      insert into restaurant values('B004','LEMONADE',150);
      insert into restaurant values('B005','OLD MONK',200);
      insert into restaurant values('B006','ROYAL CHALLENGE',230);
      insert into restaurant values('B007','BIRA 91',250);
      insert into restaurant values('B008','OFFICERS CHOICE',225);
      insert into restaurant values('B009','MCDOWELLS',300);
      insert into restaurant values('B010','BLENDERS',350);
    '''
)
conn.commit()
conn.close()
