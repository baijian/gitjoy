drop table if exists entries;
create table infos (
    id integer primary key autoincrement,
    title string not null,
    text string not null
);
