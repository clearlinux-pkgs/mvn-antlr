#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-antlr
Version  : 2.7.2
Release  : 3
URL      : https://repo1.maven.org/maven2/antlr/antlr/2.7.2/antlr-2.7.2.jar
Source0  : https://repo1.maven.org/maven2/antlr/antlr/2.7.2/antlr-2.7.2.jar
Source1  : https://repo1.maven.org/maven2/antlr/antlr/2.7.2/antlr-2.7.2.pom
Source2  : https://repo1.maven.org/maven2/antlr/antlr/2.7.7/antlr-2.7.7.jar
Source3  : https://repo1.maven.org/maven2/antlr/antlr/2.7.7/antlr-2.7.7.pom
Source4  : https://repo1.maven.org/maven2/org/antlr/antlr-master/3.4/antlr-master-3.4.pom
Source5  : https://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.4/antlr-runtime-3.4.jar
Source6  : https://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.4/antlr-runtime-3.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : ANTLR-PD BSD-3-Clause
Requires: mvn-antlr-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-antlr package.
Group: Data

%description data
data components for the mvn-antlr package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/antlr/antlr/2.7.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr-master/3.4
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr-master/3.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr-runtime/3.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr-runtime/3.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr-runtime/3.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr-runtime/3.4


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/antlr/antlr/2.7.2/antlr-2.7.2.jar
/usr/share/java/.m2/repository/antlr/antlr/2.7.2/antlr-2.7.2.pom
/usr/share/java/.m2/repository/antlr/antlr/2.7.7/antlr-2.7.7.jar
/usr/share/java/.m2/repository/antlr/antlr/2.7.7/antlr-2.7.7.pom
/usr/share/java/.m2/repository/org/antlr/antlr-master/3.4/antlr-master-3.4.pom
/usr/share/java/.m2/repository/org/antlr/antlr-runtime/3.4/antlr-runtime-3.4.jar
/usr/share/java/.m2/repository/org/antlr/antlr-runtime/3.4/antlr-runtime-3.4.pom
