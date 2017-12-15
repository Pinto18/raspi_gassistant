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
         try
	 {
            echo '========== Testing =========='
	    sh '''
	        source env/bin/activate
	        python 'src/tests/**.py'
		deactivate
	        '''
	 }
	 catch(err)
         {
	    currentBuild.Result = 'FAILURE'
	 }
	 finally
	 {
            junit 'src/tests/test-report/**.xml'
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
