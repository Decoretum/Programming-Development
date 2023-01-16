show databases;
use gaeldatabase;
show tables;
desc programmers;
select * from programmers;

update programmers
set Coursegraduated = "BS CS"
where nickname = "Justin";

select * from programmers;
desc programmers;
desc techskills;

#3 types of DML: update, delete, select

select * from programmers;
select concat(firstname," with specialization of ", Specialization) from programmers;

select concat(firstname, " is a Software Developer ") from programmers
where Specialization = "Software Development";

select distinct Specialization from programmers;

select concat(firstname, ", ", Coursegraduated) from programmers
where Coursegraduated = "BS MIS-MCS";

#comparison operators (>, <, <=, is, not, between/and, in)

select * from programmers
where Coursegraduated in ("BS MIS", "BS MIS-MCS", "BS CS")
and Specialization = "Software Development";

select * from programmers
where Specialization like "%Development";

select * from programmers
where firstname like "J%";

select * from programmers
where nickname like "%n";

show tables;

select * from Notes
where NoteHeader like "_ro%"; #programming

select * from Notes
where EditDate is Null; #not null entries

#logical operators (and, or, not)

select * from Notes
where EditDate is not null; #edited entries

select * from Notes
where NoteDate like "%2022%" and NoteID > 5;

select * from Notes
where NoteDate like "%2022%" and EditDate like "%2023%";

# Using and combining Logical and Comparison operators
# The following precedence is followed:
# ■ All comparison operators are evaluated first
# ■ All NOT
# ■ All AND
# ■ All OR
# To force the order of precedence, use ()

select * from Notes
where NoteHeader like "%Gam%"
and NoteDate like "%2022%";

#use order by <field name> desc for descending, default
#<order by> is ascending

select * from Notes
where NoteID > 4 or NoteID < 12
and NoteHeader like "%Gam%"
order by NoteID; #does not enforce precedence

select * from Notes
where (NoteID > 4 or NoteID < 12)
and NoteHeader like "%Gam%"
order by NoteID; #enforces precedence, hence limited results

show tables;

select * from game
where (Genre like "%S%");

desc game;
select * from game;

/*insert into game values ("Terraria","Sandbox","Redit","MultiForm")*/

select * from game
where (Genre = "Sandbox") and Platform = "Multiform";

select * from game
where (Platform = "Multiform") and Genre = "Sandbox";


