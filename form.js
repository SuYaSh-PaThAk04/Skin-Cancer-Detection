document.getElementById('diabetes').addEventListener('change', function() {
    const diabetesInput = this.value.toLowerCase();
    
    if (diabetesInput === 'yes') {
        document.getElementById('diabetes-details').style.display = 'block';
        
        document.getElementById('diabetes-years').addEventListener('change', function() {
            alert(`You have had diabetes for ${this.value} years.`);
        });

        document.getElementById('diabetes-level').addEventListener('change', function() {
            alert(`Your diabetes level is ${this.value}.`);
        });
        
    } else {
        document.getElementById('diabetes-details').style.display = 'none';
    }
});

document.getElementById('blood-pressure').addEventListener('change', function() {
    const bpInput = this.value.toLowerCase();
    
    if (bpInput === 'yes') {
        document.getElementById('bp-condition-details').style.display = 'block';
        
        document.getElementById('bp-condition').addEventListener('change', function() {
            alert(`Your condition is described as: ${this.value}.`);
        });
        
    } else {
        document.getElementById('bp-condition-details').style.display = 'none';
    }
});

document.getElementById('submit').addEventListener('click', function() {
    const age = document.getElementById('age').value;
    
    if (!age) {
        alert("Please enter your age.");
        return;
    }

    const diabetes = document.getElementById('diabetes').value.toLowerCase();
    
    if (diabetes === 'yes') {
        const diabetesYears = document.getElementById('diabetes-years').value;
        const diabetesLevel = document.getElementById('diabetes-level').value;

        if (!diabetesYears || !diabetesLevel) {
            alert("Please fill out all diabetes fields.");
            return;
        }
        
        alert(`You are ${age} years old and have had diabetes for ${diabetesYears} years at level ${diabetesLevel}.`);
        
    } else if (diabetes !== 'no') {
        alert("Please answer with 'yes' or 'no' for diabetes.");
        return;
    }

    const bloodPressure = document.getElementById('blood-pressure').value.toLowerCase();
    
    if (bloodPressure === 'yes') {
        const bpCondition = document.getElementById('bp-condition').value;

        if (!bpCondition) {
            alert("Please describe your blood pressure condition.");
            return;
        }

        alert(`You have blood pressure issues described as ${bpCondition}.`);
        
    } else if (bloodPressure !== 'no') {
        alert("Please answer with 'yes' or 'no' for blood pressure.");
        return;
    }

     const asthma = document.getElementById('asthma').value.toLowerCase();
     if(asthma !== "yes" && asthma !== "no") {
         alert("Please answer with 'yes' or 'no' for asthma.");
         return; 
     }

     // Blood report file check
     const bloodReportFile = document.getElementById('blood-report').files[0];
     if (!bloodReportFile) {
         alert("Please upload your blood report.");
         return; 
     }

     // Final submission message
     alert("Form submitted successfully!");
});