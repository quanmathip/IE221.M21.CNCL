'''
- Các lớp được xây dựng liên quan đến character bao gồm Person, Student, Teacher, Player.
- Sử dụng lập trình hướng đối tượng kế thừa đa cấp: Person->Studen->Player và Person->Teacher.
'''
init python:
    class Person:

        def __init__(self, character, name,point, sex, age, biography):
            self.__c = character
            self.__name = name
            self.__point = point
            self.__sex = sex
            self.__age = age
            self.__biography = biography

        @property
        def c(self):
            return self.__c
        @c.setter
        def c(self,new_c):
            self.__c = new_c
        #-----name-----
        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self,new_name):
            self.__name = new_name

        #-----sex-----
        @property
        def sex(self):
            return self.__sex
        @sex.setter
        def sex(self,new_sex):
            self.__sex = new_sex

        #-----sacrificed-----
        @property
        def sacrificed(self):
            return self.__sacrificed
        @sacrificed.setter
        def sacrificed(self,new_sacrificed):
            self.__sacrificed = new_sacrificed
        #-----biography-----
        @property
        def biography(self):
            return self.__biography
        @biography.setter
        def biography(self,new_biography):
            self.__biography = new_biography

        #-----point-----
        @property
        def point(self):
            return self.__point

        @point.setter
        def point(self, new_point):
            self.point = new_point




    class Student(Person):

        def __init__(self, character, name, point, sex, age, biography, MSSV, Degree, Class):
            Person.__init__(self,character, name, point, sex, age, biography)
            self.__MSSV = MSSV
            self.__Degree = Degree
            self.__Class = Class




        #-----------------Student-------------------------
    class Teacher(Person):

        def __init__(self,character, name,point, sex, age, biography,MSGV, Degree, Subjects):
            Person.__init__(self,character, name,point, sex, age, biography)
            self.__MSGV = MSGV
            self.__Degree = Degree
            self.__Subjects = Subjects


        #---------------------Player-----------------------
    class Player(Student):

        def __init__(self, character, name, point, sex, age, biography, MSSV, Degree, Class, health, intelligence,draw):
            Student.__init__(self,character, name, point, sex, age, biography,MSSV, Degree, Class)
            self.__health = health
            self.__intelligence = intelligence
            self.__draw = draw

#---------------------------------Create Character--------------------------------------------#
#----Player----
default player_name ="..."
define Player = Player(
                        Character("[player_name]",color="#009900",image="Player"),
                        "...",
                        0,
                        "male",
                        21,
                        "Một thanh niên wibu, sau khi được truck-sama hôn đã đc remake",
                        "STL37",
                        "Student",
                        "E3.2",
                        0,
                        0,
                        0
                        )

#----Student----
define SV_AnhDuong = Student(
                            Character("Ánh Dương"),
                            "Ánh Dương",
                            0,
                            "Female",
                            21,
                            "Ánh Dương là bạn thủa nhỏ của Player, nhà sát cạnh player",
                            "SSV001",
                            "Học Sinh",
                            "E3.2"
                            )

define SV_HoangAnh = Student(
                            Character("Hoàng Anh"),
                            "Hoàng Anh",
                            0,
                            "Male",
                            21,
                            "Là người theo đuổi Ánh Dương và khá ghét Player",
                            "SSV002",
                            "Student",
                            "E3.2"
                            )

define SV_NhatTruong = Student(
                            Character("Nhật Trường"),
                            "Nhật Trường",
                            0,
                            "Male",
                            21,
                            "Bạn thân của Player, ngầu và luôn được các bạn nữ yêu thích",
                            "SSV003",
                            "Học Sinh",
                            "E3.2"
                            )

define SV_BaoTran = Student(
                            Character("Bảo Trân"),
                            "Bảo Trân",
                            0,
                            "Female",
                            21,
                            "hotgirl lớp E3.2, thường xuyên trêu trọc Player",
                            "SSV006",
                            "Học Sinh",
                            "E3.2"
                            )

define SV_ThanhBach = Student(
                                Character("Thanh Bạch"),
                                "Thanh Bạch",
                                0,
                                "Male",
                                21,
                                "Sinh viên lớp bên rất hay trêu chọc các bạn nữ lớp E3.2",
                                "SSV007",
                                "Học Sinh",
                                "E3.1"
                                )

define SV_ThanhHai = Student(
                            Character("Thanh Hải"),
                            "Thanh Hải",
                            0,
                            "Male",
                            21,
                            "Anh em với Thanh Bạch, là 1 rickid chính hiệu",
                            "SSV008",
                            "Học Sinh",
                            "E3.1"
                            )
define SV_ThuThuy = Student(
                            Character("Thu Thủy"),
                            "Thu Thủy",
                            0,
                            "Female",
                            21,
                            "Rất ghét Player",
                            "SSV009",
                            "Học Sinh",
                            "E3.1"
                            )

#----Teacher----
define GV_AVien = Teacher(
                        Character("A Viễn"),
                        "A Viễn",
                        0,
                        "Male",
                        35,
                        "Giảng viên môn nhập môn lập trình, rất có hảo cảm với Player",
                        "SGV02",
                        "Thạc Sĩ",
                        "Nhập môn lập trình"
                        )
define GV_LongVan = Teacher(
                            Character("Long Vân"),
                            "Long Vân",
                            0,
                            "Male",
                            42,
                            "Giảng viên cấu trúc dữ liệu và giải thuật, rất hài hước và thường xuyên cho kiểm tra đột xuất",
                            "SGV03",
                            "Thạc Sĩ",
                            "cấu trúc dữ liệu và giải thuật"
                            )
define GV_HaiLi = Teacher(
                        Character("Hải Lí"),
                        "Hải Lí",
                        0,
                        "Male",
                        26,
                        "Giảng viên thể dục",
                        "SGV04",
                        "Cử Nhân",
                        "Thể Dục"
                        )
define GV_BaQuan = Teacher(
                            Character("Bá Quân"),
                            "Bá Quân",
                            0,
                            "Male",
                            28,
                            "Giảng viên lập trình hướng đôi tượng",
                            "SGV05",
                            "Thạc Sĩ",
                            "Lập trình hướng đối tượng"
                            )
define GV_ThanhThao = Teacher(
                            Character("Thanh Thảo"),
                            "Thanh Thảo",
                            0,
                            "Female",
                            35,
                            "Giảng viên môn nhập môn lập trình web, có hảo cảm với Player",
                            "SGV06",
                            "Thạc Sĩ",
                            "Nhập môn lập trình web"
                            )
define GV_NgocNhu = Teacher(
                            Character("Ngọc Như"),
                            "Ngọc Như",
                            0,
                            "Female",
                            26,
                            "Giảng viên kỹ thuật lập trình python",
                            "SGV07",
                            "Giảng Viên",
                            "Nhập môn kỹ thuật lập trình python"
                            )
define HT_VanSon = Teacher(
                            Character("Văn Sơn"),
                            "Văn Sơn",
                            0,
                            "Male",
                            55,
                            "Hiệu trưởng luôn vui vẻ và có chút nghiêm khắc",
                            "SGV08",
                            "Tiến Sĩ",
                            "An Toàn Thông Tin"
                            )

#----Staff----
define NV_NgocAnh = Person(
                            Character("Ngọc Anh"),
                            "Ngọc Anh",
                            0,
                            "Female",
                            28,
                            "Ý tá của trường"
                            )
define NV_NhuQuynh = Person(
                            Character("Như Quỳnh"),
                            "Như Quỳnh",
                            0,
                            "Female",
                            35,
                            "Lao Công"
                            )
#---------Character-------------
define Daion = Character("Daion",image = "vatchu.gif")
define Mama = Person(
                    Character("Mama"),
                    "Mama",
                    0,
                    "female",
                    42,
                    "sdsds"
                    )
