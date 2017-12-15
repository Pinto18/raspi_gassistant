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
            def installed = fileExists 'env/bin/activate'
	    echo '========== Building =========='
            if(!installed)
            {
               sh 'virtual env --no-site-packages .'
            } 
	 }
      }
      stage('Test')
      {
          def testError = null
         steps
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
	       testError = err
	       currentBuild.Result = 'FAILURE'
	    }
	    finally
	    {
	       junit 'src/tests/test-report/**.xml'
	       if(testError)
	       {
	          throw testError
	       }
	    }
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
