create view `PARTICIPANT_INFO` (`ID`, `CH_Name`, `EN_Name`, `Phone`, `Mail`, 
								`Identity`, `Units`, `JobTitle`, `MemberId`, 
                                `FileName`, `Pay_time`, `Price`, `Account`, 
                                `Address`, `isCheck`, `Remark`)
as
select `ID`, `CH_Name`, `EN_Name`, `Phone`, `Mail`, 
	   `Identity`, `Units`, `JobTitle`, `MemberId`, 
	   `FileName`, `Pay_time`, `Price`, `Account`, 
       `Address`, `isCheck`, `Remark`
from   `PARTICIPANT`, `RECEIPT`
where  `ID`=`Owner`;