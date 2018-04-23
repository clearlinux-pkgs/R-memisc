#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-memisc
Version  : 0.99.14.9
Release  : 5
URL      : https://cran.r-project.org/src/contrib/memisc_0.99.14.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/memisc_0.99.14.9.tar.gz
Summary  : Management of Survey Data and Presentation of Analysis Results
Group    : Development/Tools
License  : GPL-2.0
Requires: R-memisc-lib
Requires: R-car
Requires: R-repr
BuildRequires : R-car
BuildRequires : R-repr
BuildRequires : clr-R-helpers

%description
value labels, definable missing values, recoding of variables,
        production of code books, and import of (subsets of) 'SPSS' and
        'Stata' files is provided. Further, the package allows to produce
        tables and data frames of arbitrary descriptive statistics and
        (almost) publication-ready tables of regression model
        estimates, which can be exported to 'LaTeX' and HTML.

%package lib
Summary: lib components for the R-memisc package.
Group: Libraries

%description lib
lib components for the R-memisc package.


%prep
%setup -q -c -n memisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523318039

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523318039
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library memisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library memisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library memisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library memisc|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/memisc/ChangeLog
/usr/lib64/R/library/memisc/DESCRIPTION
/usr/lib64/R/library/memisc/INDEX
/usr/lib64/R/library/memisc/Meta/Rd.rds
/usr/lib64/R/library/memisc/Meta/features.rds
/usr/lib64/R/library/memisc/Meta/hsearch.rds
/usr/lib64/R/library/memisc/Meta/links.rds
/usr/lib64/R/library/memisc/Meta/nsInfo.rds
/usr/lib64/R/library/memisc/Meta/package.rds
/usr/lib64/R/library/memisc/Meta/vignette.rds
/usr/lib64/R/library/memisc/NAMESPACE
/usr/lib64/R/library/memisc/NEWS.Rd
/usr/lib64/R/library/memisc/R/memisc
/usr/lib64/R/library/memisc/R/memisc.rdb
/usr/lib64/R/library/memisc/R/memisc.rdx
/usr/lib64/R/library/memisc/anes/NES1948.ZIP
/usr/lib64/R/library/memisc/doc/anes48.R
/usr/lib64/R/library/memisc/doc/anes48.Rmd
/usr/lib64/R/library/memisc/doc/anes48.html
/usr/lib64/R/library/memisc/doc/ftable-matrix.R
/usr/lib64/R/library/memisc/doc/ftable-matrix.Rmd
/usr/lib64/R/library/memisc/doc/ftable-matrix.html
/usr/lib64/R/library/memisc/doc/index.html
/usr/lib64/R/library/memisc/doc/items.R
/usr/lib64/R/library/memisc/doc/items.Rmd
/usr/lib64/R/library/memisc/doc/items.html
/usr/lib64/R/library/memisc/doc/mtable-html.R
/usr/lib64/R/library/memisc/doc/mtable-html.Rmd
/usr/lib64/R/library/memisc/doc/mtable-html.html
/usr/lib64/R/library/memisc/gles/gles2013work.RData
/usr/lib64/R/library/memisc/help/AnIndex
/usr/lib64/R/library/memisc/help/aliases.rds
/usr/lib64/R/library/memisc/help/memisc.rdb
/usr/lib64/R/library/memisc/help/memisc.rdx
/usr/lib64/R/library/memisc/help/paths.rds
/usr/lib64/R/library/memisc/html/00Index.html
/usr/lib64/R/library/memisc/html/R.css
/usr/lib64/R/library/memisc/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/memisc/libs/memisc.so
/usr/lib64/R/library/memisc/libs/memisc.so.avx2
/usr/lib64/R/library/memisc/libs/memisc.so.avx512
