create table `PARTICIPANT` (
	`ID`          int            not null,
    `CH_Name`     varchar(10)    not null,
    `EN_Name`     varchar(20)    not null,
    `Phone`       char(10)       not null,
    `Address`     text,
    `Units`       text,
    `JobTitle`    text,
    `TaxIdNum`    char(8),
    `MemberId`    varchar(11),
    `Price`       int,
    `JoinTime`    date           not null,
    `Mail`        text           not null,
    `Identity`    char(7)        not null    check(`Identity`='teacher' or `Identity`='student'),
    primary key (`ID`)
);

create table `PAPER` (
	`PaperId`    int        not null,
    `Title`      text,
    `Time`       date       not null,
    `Author`     text,
    `isPass`     boolean    default(false)    not null,
    `Owner`      int,
    primary key (`PaperId`),
    foreign key (`Owner`) references `PARTICIPANT`(`ID`)
);

create table `RECEIPT` (
	`Owner`       int        not null,
    `FileName`    int        not null,
    `Account`     char(5)    not null,
    `Pay_time`    date       not null,
    `Remark`      boolean    default(false),
    `isCheck`     boolean    default(false),
    primary key (`Owner`, `FileName`),
    foreign key (`Owner`) references `PARTICIPANT`(`ID`)
);