#! /usr/bin/perl
use strict;

#print "Hello\n";
#print $ENV{"PWD"},"\n";
#foreach (@ll)
#{
#	print "$_\n";
#}
if( @ARGV <= 1)
{
#	print $ARGV[0],"\n";
#	my $dir = $ARGV[0];
	my @files = <*>;
	if( @ARGV == 1)
	{
		@files = glob("$ARGV[0]/*");
	}
#else
#	{
#		my @files = <*>;
#	}

	foreach my $file (@files)
	{
#		print $file ;
		if( -f $file)
		{
			;
#	print "\t it is a file\n";
		}
		else
		{
			print "$file\n"; 
#print $file . "\n";
		}
	}
}
else
{
	print "Error only one or zero arguments are accepted\n";
}
