show databases;
use gaeldatabase;
show tables;
desc notes;

/* alter table notes add column NoteHeader varchar(100) not null; */

alter table notes 
modify NoteBody varchar(200) not null;
desc notes;

/*insert into notes
values (0,'Lol I stepped on a bee','Fun Experience');*/

select * from notes;