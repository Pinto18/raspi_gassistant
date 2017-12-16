#!usr/bin/envy/groovy

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
	    bat 'python tests/test-api-integrations.py'
            junit 'test-report/**.xml'
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
