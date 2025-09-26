pipeline {
  agent any

  environment {
    # 改成你的 Python 可执行文件路径（例：C:\\Users\\86150\\AppData\\Local\\Programs\\Python\\Python311\\python.exe）
    PYTHON_PATH = "C:\\Users\\86150\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
  }

  stages {
    stage("Checkout") {
      steps {
        // 如果你用 HTTPS + 用户名/Token，建议加 credentialsId
        // 先在 Jenkins 全局凭据里新建一个 ID（例如 github-credentials）
        git url: "https://github.com/你的GitHub用户名/你的仓库名.git",
            branch: "main",
            credentialsId: "github-credentials"
      }
    }

    stage("Fix pip") {
      steps {
        bat """
          @echo off
          %PYTHON_PATH% -m ensurepip --upgrade
          %PYTHON_PATH% -m pip --version
        """
      }
    }

    stage("Install Deps") {
      steps {
        bat """
          %PYTHON_PATH% -m pip install --upgrade pip
          %PYTHON_PATH% -m pip install -r requirements.txt
        """
      }
    }

    stage("Lint") {
      steps {
        bat "%PYTHON_PATH% -m flake8 app.py tests/"
      }
    }

    stage("Test") {
      steps {
        bat """
          %PYTHON_PATH% -m pytest --cov=app tests/ --cov-report=html
        """
      }
      post {
        always {
          publishHTML(target: [
            reportDir: 'htmlcov',
            reportFiles: 'index.html',
            reportName: 'Coverage Report',
            keepAll: true,
            alwaysLinkToLastBuild: false,
            allowMissing: true
          ])
        }
      }
    }

    stage("Build (optional)") {
      steps {
        bat """
          %PYTHON_PATH% -m pip install pyinstaller
          %PYTHON_PATH% -m PyInstaller --onefile app.py
        """
      }
    }

    stage("Deploy (demo)") {
      steps {
        echo "Deploying application (demo)..."
        // 真部署按你的需求实现（IIS/Docker/复制到服务器/SSH 等）
      }
    }
  }

  post {
    success { echo "CI/CD pipeline completed successfully!" }
    failure { echo "CI/CD pipeline failed!" }
  }
}
