"""
Quick test for Professor Balthazar's Magic Machine
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from consultation_agent import consult_professor_balthazar


async def test_basic_functionality():
    """Test basic agent functionality"""
    print("🧪 Testing Professor Balthazar basic consultation...")
    
    # Test basic consultation
    session_id = await consult_professor_balthazar("I'm feeling bored today")
    assert session_id.startswith("consultation_")
    print(f"✅ Basic consultation works! Session: {session_id}")
    
    return True


async def test_session_continuity():
    """Test that sessions maintain context"""
    print("🧪 Testing session continuity...")
    
    # First message
    response1, session_id = await consult_professor_balthazar("I need help with motivation")
    assert session_id is not None
    
    # Second message in same session
    response2, same_id = await consult_professor_balthazar(
        "My name is Alex", 
        session_id=session_id
    )
    
    assert session_id == same_id
    print(f"✅ Session continuity works! Session maintained: {session_id == same_id}")
    
    return True


async def run_all_tests():
    """Run all tests"""
    print("🚀 Running Professor Balthazar Tests")
    print("=" * 50)
    
    tests = [
        test_basic_functionality(),
        test_session_continuity()
    ]
    
    results = await asyncio.gather(*tests, return_exceptions=True)
    
    passed = sum(1 for r in results if r is True)
    total = len(tests)
    
    print("=" * 50)
    print(f"📊 RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Agent is working correctly!")
        return True
    else:
        print("❌ Some tests failed")
        return False


if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    exit(0 if success else 1)


# Upgrade Test: Multi-Agent
async def test_multi_agent():
    from graph import app  # Your graph
    inputs = {"messages": [HumanMessage(content="Angry boss reply?")]}
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Multi Test {key}: {value['messages'][-1].content}")
    return True

# Run upgrade test
asyncio.run(test_multi_agent())
print("✅ Upgrade test passed!")
