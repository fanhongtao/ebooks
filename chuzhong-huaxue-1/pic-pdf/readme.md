
* [czhx1-periodictable.tex]: 生成元素周期表的 TeX 代码
* [pgfPT.lang.nl.tex]: 生成 “元素周期表” 时，供 [pgf-PeriodicTable](https://ctan.org/pkg/pgf-periodictable) 宏包使用的语言包。

由于 `pgf-PeriodicTable` 宏包暂不支持中文，所以先**借用**宏包已经提供的一个语言包 `pgfPT.lang.nl.tex`，将其（部分）内容修改成中文后，存放在这里。

在编译 `czhx1-periodictable.tex` 前，需要将 `pgfPT.lang.nl.tex` 拷贝到 `translations` 目录下，覆盖原有的文件。

> 1. 在我的电脑上，`pgf-PeriodicTable` 宏包的语言包对应的目录为：`C:\texlive\2024\texmf-dist\tex\latex\pgf-periodictable\translations`。<br/>
> 2. 拷贝前，可以先备份 `translations` 目录下的 `pgfPT.lang.nl.tex` 文件。


等  `pgf-PeriodicTable` 宏包自身支持提供了中文的语言包后，就可以删除 `pgfPT.lang.nl.tex`，并将 `czhx1-periodictable.tex]` 修改为使用中文的语言包。


