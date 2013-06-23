#!/usr/bin/env perl

use File::Spec::Functions qw(rel2abs);
use File::Basename qw(dirname);

print dirname( rel2abs( __FILE__ ) );
