pipeline
{
   agent any

   stages
   {
      stage('Build')
      {
         steps
	 {
	    echo '========== Building =========='
	 }
      }
      stage('Test')
      {
         steps
	 {
	    echo '========== Testing =========='
	    python 'src/tests/**.py'
	    junit 'src/tests/test-reports/**.xml'
	 }
      }
      stage('Deploy')
      {
         steps
	 {
	    echo '========== Deploying =========='
	 }
      }
   }
}
