#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-memisc
Version  : 0.99.31.7
Release  : 65
URL      : https://cran.r-project.org/src/contrib/memisc_0.99.31.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/memisc_0.99.31.7.tar.gz
Summary  : Management of Survey Data and Presentation of Analysis Results
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-memisc-lib = %{version}-%{release}
Requires: R-data.table
Requires: R-jsonlite
Requires: R-yaml
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : R-yaml
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n memisc
pushd ..
cp -a memisc buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702277939

%install
export SOURCE_DATE_EPOCH=1702277939
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/memisc/libs/memisc.so
/usr/lib64/R/library/memisc/libs/memisc.so.avx2
/usr/lib64/R/library/memisc/libs/memisc.so.avx512
